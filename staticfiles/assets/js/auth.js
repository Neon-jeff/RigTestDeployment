const pswdInput = document.querySelector('.pswd-input');
const showPswd = document.querySelector('.show-pswd');
const hidePswd = document.querySelector('.hide-pswd');

// SHOW PASSWORD
showPswd.addEventListener('click', () => {
	pswdInput.type = 'text';
	hidePswd.classList.remove('hidden');
	showPswd.classList.add('hidden');
});

// HIDE PASSWORD
hidePswd.addEventListener('click', () => {
	pswdInput.type = 'password';
	showPswd.classList.remove('hidden');
	hidePswd.classList.add('hidden');
});
