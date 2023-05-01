const navContainer = document.querySelector('.navbar');
const header = document.querySelector('.header__wrapper');

// ============= INTERSECTION OBSERVER ================
const options = {
	rootMargin: '0px',
	threshold: 0.2,
};

let observer = new IntersectionObserver((entries) => {
	entries.forEach((entry) => {
		if (entry.isIntersecting) {
			navContainer.classList.remove('header-bg');
		} else {
			navContainer.classList.add('header-bg');
		}
	});
}, options);

observer.observe(header);
