//================ SCROLLREVEAL ================
import ScrollReveal from 'scrollreveal';
ScrollReveal.debug = true;

// ========== NAVIGATION TOGGLE =============
const navBar = document.querySelector('.main-nav');
const toggle = document.querySelector('.nav-toggle');

// ================ SEARCH EVENTS ====================
const searchIcons = document.querySelectorAll('.toggle-form');
const closeIcon = document.querySelector('.event-close');
const searchInput = document.querySelector('.event-search');

// ========= DISPLAY FORM INPUT ====================
searchIcons.forEach((searchIcon) => {
	searchIcon.addEventListener('click', () => {
		searchInput.classList.remove('hidden');
		document.querySelector('.search-form__input').focus();
		hideNavbar();

		CloseOnKeyPress();
	});
});

// ========================= HIDE FORM INPUT FUNCTION ==================
function CloseOnKeyPress() {
	// HIDE FORM BY CLICKING X
	closeIcon.addEventListener('click', () => {
		hideSearchBar();
	});

	// HIDE FORM WITH ESC KEY
	document.addEventListener('keydown', (e) => {
		if (e.key === 'Escape') {
			hideSearchBar();
		}
	});
}

function hideSearchBar() {
	searchInput.classList.add('hidden');
}

function hideNavbar() {
	navBar.classList.add('hide-nav');
}

// NAVBAR TOGGLE
toggle.addEventListener('click', (e) => {
	navBar.classList.toggle('hide-nav');
	hideSearchBar();
});

// ============= CONTACT PAGE ANIMATION =============
ScrollReveal().reveal('.center-img', {
	duration: 800,
	delay: 500,
	cleanup: true,
});

ScrollReveal().reveal('.top-img', {
	duration: 800,
	delay: 800,
	cleanup: true,
});

ScrollReveal().reveal('.bottom-img', {
	duration: 800,
	delay: 1000,
});

// ============== MERCH CARD ===============
const shopCards = document.querySelectorAll('.shop__card');

ScrollReveal().reveal(shopCards, {
	duration: 1000,
	delay: 100,
	interval: 200,
});

// ============== EVENTS CARD ===============
const eventCards = document.querySelectorAll('.event');

ScrollReveal().reveal(eventCards, {
	duration: 800,
	distance: '150%',
	cleanup: true,
	delay: 100,
	interval: 200,
});

// ============ LANDING PAGE ANIMATIONS ==============
// welcome section
const welcomeText = document.querySelector('.welcome__txt');
const welcomeImg = document.querySelector('.welcome__img');

ScrollReveal().reveal(welcomeText, {
	duration: 800,
	distance: '150%',
	delay: 100,
	origin: 'left',
});

ScrollReveal().reveal(welcomeImg, {
	duration: 900,
	distance: '150%',
	delay: 200,
	origin: 'right',
});

//  partners__card (landing page)
const partnersCard = document.querySelectorAll('.partners__card');

ScrollReveal().reveal(partnersCard, {
	duration: 900,
	distance: '150%',
	delay: 100,
	origin: 'left',
	interval: 200,
});

// ============ RIGX PAGE ANIMATIONS ==============
// contact cards
const rigXCard = document.querySelectorAll('.contact');

ScrollReveal().reveal(rigXCard, {
	duration: 900,
	distance: '150%',
	delay: 100,
	origin: 'bottom',
	interval: 200,
});

// ==================== TOGGLE DONATION MODAL =================
const showDonationBTN = document.querySelectorAll('.show-modal');
const closeDonation = document.querySelector('.close-donation');
const donationWrapper = document.querySelector('.donation__wrapper');

// show modal
showDonationBTN.forEach((showDonation) => {
	showDonation.addEventListener('click', () => {
		donationWrapper.classList.toggle('hidden');
		// also hide navbar when modal is open
		hideNavbar();
	});
});

// hide modal
closeDonation.addEventListener('click', () => {
	donationWrapper.classList.add('hidden');
});
