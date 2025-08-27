(function(){
	const $ = (sel, root=document) => root.querySelector(sel)
	const $$ = (sel, root=document) => Array.from(root.querySelectorAll(sel))

	function toast(msg, type){
		const c = document.createElement('div')
		c.className = 'toast'
		c.textContent = msg
		$('#toast')?.appendChild(c)
		setTimeout(()=>{ c.style.opacity='0'; setTimeout(()=>c.remove(), 200)}, 2400)
	}

	// Create form: toggle expiry
	const lifetimeRadios = $$('form[action="/admin/keys"] input[name="key_type"]')
	const createExpiry = $('#create-expiry-wrap')
	function updateCreateExpiry(){
		const type = lifetimeRadios.find(r=>r.checked)?.value
		createExpiry.style.display = type==='short' ? '' : 'none'
	}
	lifetimeRadios.forEach(r=>r.addEventListener('change', updateCreateExpiry))
	updateCreateExpiry()

	// Edit modal
	const editModal = $('#edit-modal')
	const editForm = $('#edit-form')
	const editExpiryWrap = $('#edit-expiry-wrap')
	$$('[data-edit]').forEach(btn=>{
		btn.addEventListener('click', ()=>{
			const data = JSON.parse(btn.getAttribute('data-edit'))
			$('#edit-key-name').value = data.key_name
			editForm.setAttribute('action', `/admin/keys/${data.id}`)
			const lifetime = data.is_lifetime === 1
			editForm.querySelector('input[value="lifetime"]').checked = lifetime
			editForm.querySelector('input[value="short"]').checked = !lifetime
			if(lifetime){
				editExpiryWrap.style.display='none'
				$('#edit-expires').value = ''
			}else{
				editExpiryWrap.style.display=''
				// convert ISO to datetime-local
				if(data.expires_at){
					try{
						const d = new Date(data.expires_at)
						const pad = n=>String(n).padStart(2,'0')
						const local = `${d.getUTCFullYear()}-${pad(d.getUTCMonth()+1)}-${pad(d.getUTCDate())}T${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}`
						$('#edit-expires').value = local
					}catch(e){ $('#edit-expires').value = '' }
				}
			}
			$('#edit-note').value = data.note || ''
			editModal.setAttribute('aria-hidden','false')
		})
	})
	$$('#edit-modal [data-close]').forEach(b=> b.addEventListener('click', ()=> editModal.setAttribute('aria-hidden','true')))
	$('#edit-modal .modal-backdrop')?.addEventListener('click', ()=> editModal.setAttribute('aria-hidden','true'))

	editForm?.querySelectorAll('input[name="key_type"]').forEach(r=>{
		r.addEventListener('change', ()=>{
			const type = editForm.querySelector('input[name="key_type"]:checked').value
			editExpiryWrap.style.display = type==='short' ? '' : 'none'
		})
	})

	// Double confirm delete
	window.confirmDelete = function(ev){
		if(!ev.target.closest('form')) return true
		ev.preventDefault()
		const form = ev.target.closest('form')
		const m = $('#confirm-modal')
		m.setAttribute('aria-hidden','false')
		$('#confirm-step-2').onclick = ()=>{
			const f2 = document.createElement('form')
			f2.method = 'post'
			f2.action = form.action
			const s1 = document.createElement('input')
			s1.type = 'hidden'; s1.name='confirm_step'; s1.value='1'
			const s2 = document.createElement('input')
			s2.type = 'hidden'; s2.name='confirm_step'; s2.value='2'
			f2.appendChild(s1); f2.appendChild(s2)
			document.body.appendChild(f2)
			f2.submit()
		}
		m.querySelector('[data-close]').onclick = ()=> m.setAttribute('aria-hidden','true')
		m.querySelector('.modal-backdrop').onclick = ()=> m.setAttribute('aria-hidden','true')
		return false
	}

	// Flash as toast clone (optional UX)
	const flashes = document.querySelectorAll('.flash')
	if(flashes.length){
		flashes.forEach(f=> toast(f.textContent))
	}
})()