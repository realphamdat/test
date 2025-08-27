-- SQLite schema for API keys
-- Run manually: sqlite3 keys.sqlite3 < schema.sql

PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS api_keys (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	key_name TEXT NOT NULL UNIQUE,
	is_lifetime INTEGER NOT NULL DEFAULT 0,
	expires_at TEXT,
	note TEXT,
	created_at TEXT NOT NULL,
	updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_api_keys_key_name ON api_keys (key_name);
CREATE INDEX IF NOT EXISTS idx_api_keys_expires_at ON api_keys (expires_at);