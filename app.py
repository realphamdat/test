import sqlite3
import json
from datetime import datetime, timezone
from functools import wraps
from io import BytesIO
import zipfile

from flask import (
	Flask, render_template, request, redirect, url_for, session,
	flash, send_file, jsonify
)

# App setup: reads secret from data/setting.json; does not create files/dirs
with open('data/setting.json', 'r', encoding='utf-8') as f:
	SETTINGS = json.load(f)

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = SETTINGS.get('secret_key', '')

DB_PATH = 'keys.sqlite3'
CODE_PATH = 'data/code.txt'
ASSETS_PATH = 'data/assets.zip'

# --- Helpers ---

def get_db_connection():
	# DB file must exist; this function does not create it
	conn = sqlite3.connect(DB_PATH)
	conn.row_factory = sqlite3.Row
	return conn


def require_login(view_func):
	@wraps(view_func)
	def wrapper(*args, **kwargs):
		if not session.get('admin_logged_in'):
			return redirect(url_for('login', next=request.path))
		return view_func(*args, **kwargs)
	return wrapper


def utcnow_iso() -> str:
	return datetime.now(timezone.utc).isoformat()


def parse_dt_local(dt_str):
	if not dt_str:
		return None
	try:
		dt = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M')
		return dt.replace(tzinfo=timezone.utc).isoformat()
	except ValueError:
		return None


def is_expired(row) -> bool:
	if row['is_lifetime']:
		return False
	expires_at = row['expires_at']
	if not expires_at:
		return True
	try:
		dt = datetime.fromisoformat(expires_at)
		return datetime.now(timezone.utc) > dt
	except Exception:
		return True


def compare_versions(client: str, latest: str) -> int:
	# returns -1 if client < latest, 0 if ==, 1 if >
	def parse(v):
		return [int(x) for x in v.split('.') if x.isdigit()]
	ca, la = parse(client), parse(latest)
	for a, b in zip(ca, la):
		if a < b:
			return -1
		if a > b:
			return 1
	if len(ca) < len(la) and any(b != 0 for b in la[len(ca):]):
		return -1
	if len(ca) > len(la) and any(a != 0 for a in ca[len(la):]):
		return 1
	return 0


# --- Auth ---

@app.get('/login')
def login():
	if session.get('admin_logged_in'):
		return redirect(url_for('admin_dashboard'))
	return render_template('login.html')


@app.post('/login')
def login_post():
	password = request.form.get('password', '')
	if password == SETTINGS.get('password', ''):
		session['admin_logged_in'] = True
		flash('Welcome back.', 'success')
		next_url = request.args.get('next') or url_for('admin_dashboard')
		return redirect(next_url)
	flash('Invalid password.', 'error')
	return redirect(url_for('login'))


@app.post('/logout')
@require_login
def logout():
	session.clear()
	flash('Logged out.', 'info')
	return redirect(url_for('login'))


# --- Admin UI ---

@app.get('/')
@require_login
def admin_dashboard():
	q = (request.args.get('q') or '').strip()
	status = (request.args.get('status') or 'all').strip()

	conn = get_db_connection()
	rows = conn.execute('SELECT * FROM api_keys ORDER BY created_at DESC').fetchall()
	conn.close()

	keys = []
	for r in rows:
		row = dict(r)
		row['expired'] = is_expired(r)
		keys.append(row)

	def matches(row):
		if q:
			needle = q.lower()
			if needle not in row['key_name'].lower() and needle not in (row.get('note') or '').lower():
				return False
		if status == 'active' and row['expired']:
			return False
		if status == 'expired' and not row['expired']:
			return False
		return True

	filtered = [k for k in keys if matches(k)]

	return render_template('admin.html',
		keys=filtered,
		query=q,
		status=status,
		latest_version=SETTINGS.get('version', '0.0.0')
	)


@app.post('/admin/keys')
@require_login
def create_key():
	key_name = (request.form.get('key_name') or '').strip()
	kind = request.form.get('key_type')
	note = (request.form.get('note') or '').strip()

	if not key_name:
		flash('Key name is required.', 'error')
		return redirect(url_for('admin_dashboard'))

	is_lifetime = 1 if kind == 'lifetime' else 0
	expires_at = None
	if not is_lifetime:
		expires_at = parse_dt_local(request.form.get('expires_at'))
		if not expires_at:
			flash('Valid expiration date/time is required for short-term keys.', 'error')
			return redirect(url_for('admin_dashboard'))

	conn = get_db_connection()
	try:
		conn.execute(
			'INSERT INTO api_keys (key_name, is_lifetime, expires_at, note, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)',
			(key_name, is_lifetime, expires_at, note, utcnow_iso(), utcnow_iso())
		)
		conn.commit()
		flash('Key created.', 'success')
	except sqlite3.IntegrityError:
		flash('Key name already exists.', 'error')
	finally:
		conn.close()
	return redirect(url_for('admin_dashboard'))


@app.post('/admin/keys/<int:key_id>')
@require_login
def update_key(key_id: int):
	# key_name immutable
	kind = request.form.get('key_type')
	note = (request.form.get('note') or '').strip()
	is_lifetime = 1 if kind == 'lifetime' else 0
	expires_at = None
	if not is_lifetime:
		expires_at = parse_dt_local(request.form.get('expires_at'))
		if not expires_at:
			flash('Valid expiration date/time is required for short-term keys.', 'error')
			return redirect(url_for('admin_dashboard'))

	conn = get_db_connection()
	conn.execute(
		'UPDATE api_keys SET is_lifetime=?, expires_at=?, note=?, updated_at=? WHERE id=?',
		(is_lifetime, expires_at, note, utcnow_iso(), key_id)
	)
	conn.commit()
	conn.close()
	flash('Key updated.', 'success')
	return redirect(url_for('admin_dashboard'))


@app.post('/admin/keys/<int:key_id>/delete')
@require_login
def delete_key(key_id: int):
	steps = request.form.getlist('confirm_step')
	if not ('1' in steps and '2' in steps):
		flash('Deletion cancelled.', 'info')
		return redirect(url_for('admin_dashboard'))
	conn = get_db_connection()
	conn.execute('DELETE FROM api_keys WHERE id=?', (key_id,))
	conn.commit()
	conn.close()
	flash('Key deleted.', 'success')
	return redirect(url_for('admin_dashboard'))


# --- API ---

@app.post('/api/check')
def api_check():
	try:
		payload = request.get_json(force=True, silent=False)
	except Exception:
		return jsonify({'ok': False, 'reason': 'bad_request'}), 400

	key_name = (payload.get('key') or '').strip()
	client_version = (payload.get('version') or '').strip()
	if not key_name or not client_version:
		return jsonify({'ok': False, 'reason': 'bad_request'}), 400

	conn = get_db_connection()
	row = conn.execute('SELECT * FROM api_keys WHERE key_name=?', (key_name,)).fetchone()
	conn.close()
	if row is None:
		return jsonify({'ok': False, 'reason': 'invalid'}), 401
	if is_expired(row):
		return jsonify({'ok': False, 'reason': 'expired'}), 403

	latest = SETTINGS.get('version', '0.0.0')
	cmp = compare_versions(client_version, latest)

	if cmp < 0:
		# client is outdated: return zip containing code.txt and assets.zip
		buf = BytesIO()
		with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
			with open(CODE_PATH, 'rb') as f:
				zf.writestr('code.txt', f.read())
			with open(ASSETS_PATH, 'rb') as f:
				zf.writestr('assets.zip', f.read())
		buf.seek(0)
		return send_file(
			buf,
			mimetype='application/zip',
			as_attachment=True,
			download_name=f'update_{latest}.zip'
		)
	else:
		# latest or newer: return only code.txt
		return send_file(CODE_PATH, mimetype='text/plain', as_attachment=True, download_name='code.txt')


# --- Error handlers ---

@app.errorhandler(404)
def not_found(e):
	return render_template('error.html', code=404, message='Page not found'), 404


@app.errorhandler(500)
def server_error(e):
	return render_template('error.html', code=500, message='Server error'), 500


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=False)