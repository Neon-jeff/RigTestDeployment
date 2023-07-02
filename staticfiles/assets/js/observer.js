const navContainer = document.querySelector('.navbar');
const header = document.querySelector('.header__wrapper');
const newsline = document.querySelector('.newsline');

// ============= INTERSECTION OBSERVER ================
const options = {
	rootMargin: '0px',
	threshold: 0.2,
};

let observer = new IntersectionObserver((entries) => {
	entries.forEach((entry) => {
		if (entry.isIntersecting) {
			navContainer.classList.remove('header-bg');
			newsline.classList.remove('hidden');
			navContainer.style.top = 'inherit';
		} else {
			navContainer.classList.add('header-bg');
			newsline.classList.add('hidden');
			navContainer.style.top = 0;
		}
	});
}, options);

observer.observe(header);
