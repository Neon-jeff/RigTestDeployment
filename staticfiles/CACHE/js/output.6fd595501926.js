ScrollReveal.debug=true;const navBar=document.querySelector('.main-nav');const toggle=document.querySelector('.nav-toggle');const searchIcons=document.querySelectorAll('.toggle-form');const closeIcon=document.querySelector('.event-close');const searchInput=document.querySelector('.event-search');searchIcons.forEach((searchIcon)=>{searchIcon.addEventListener('click',()=>{searchInput.classList.remove('hidden');document.querySelector('.search-form__input').focus();hideNavbar();CloseOnKeyPress();});});function CloseOnKeyPress(){closeIcon.addEventListener('click',()=>{hideSearchBar();});document.addEventListener('keydown',(e)=>{if(e.key==='Escape'){hideSearchBar();}});}
function hideSearchBar(){searchInput.classList.add('hidden');}
function hideNavbar(){navBar.classList.add('hide-nav');}
toggle.addEventListener('click',(e)=>{navBar.classList.toggle('hide-nav');hideSearchBar();});ScrollReveal().reveal('.center-img',{duration:800,delay:500,cleanup:true,});ScrollReveal().reveal('.top-img',{duration:800,delay:800,cleanup:true,});ScrollReveal().reveal('.bottom-img',{duration:800,delay:1000,});const shopCards=document.querySelectorAll('.shop__card');ScrollReveal().reveal(shopCards,{duration:1000,delay:100,interval:200,});const eventCards=document.querySelectorAll('.event');ScrollReveal().reveal(eventCards,{duration:800,distance:'150%',cleanup:true,delay:100,interval:200,});const welcomeText=document.querySelector('.welcome__txt');const welcomeImg=document.querySelector('.welcome__img');ScrollReveal().reveal(welcomeText,{duration:800,distance:'150%',delay:100,origin:'left',});ScrollReveal().reveal(welcomeImg,{duration:900,distance:'150%',delay:200,origin:'right',});const partnersCard=document.querySelectorAll('.partners__card');ScrollReveal().reveal(partnersCard,{duration:900,distance:'150%',delay:100,origin:'left',interval:200,});const rigXCard=document.querySelectorAll('.contact');ScrollReveal().reveal(rigXCard,{duration:900,distance:'150%',delay:100,origin:'bottom',interval:200,});const showDonationBTN=document.querySelectorAll('.show-modal');const closeDonation=document.querySelector('.close-donation');const donationWrapper=document.querySelector('.donation__wrapper');showDonationBTN.forEach((showDonation)=>{showDonation.addEventListener('click',()=>{donationWrapper.classList.toggle('hidden');hideNavbar();});});closeDonation.addEventListener('click',()=>{donationWrapper.classList.add('hidden');});;const pswdInput=document.querySelector('.pswd-input');const showPswd=document.querySelector('.show-pswd');const hidePswd=document.querySelector('.hide-pswd');showPswd.addEventListener('click',()=>{pswdInput.type='text';hidePswd.classList.remove('hidden');showPswd.classList.add('hidden');});hidePswd.addEventListener('click',()=>{pswdInput.type='password';showPswd.classList.remove('hidden');hidePswd.classList.add('hidden');});;