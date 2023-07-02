const swiper = new Swiper('.slide-content', {
	// Optional parameters
	direction: 'horizontal',
	loop: true,
	grabCursor: true,
	slidesPerView: 'auto',
	spaceBetween: 25,
	centeredSlides: true,
	fade: true,
	autoplay: {
		delay: 2500,
		disableOnInteraction: false,
	},
	breakpoints: {
		640: {
			slidesPerView: 1,
			// spaceBetween: 15,
		},
		768: {
			slidesPerView: 2,
			// spaceBetween: 15,
		},
		1024: {
			slidesPerView: 3,
			// spaceBetween: 15,
		},
	},
	pagination: {
		el: '.swiper-pagination',
		clickable: true,
		dynamicBullets: true,
	},
});
