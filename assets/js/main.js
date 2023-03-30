/**
* Template Name: eNno - v4.3.0
* Template URL: https://bootstrapmade.com/enno-free-simple-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  var button = document.getElementById("book-service-btn");
  const logoTitle =document.querySelector ('.logo-title');

  // Add a scroll event listener to the window
  window.addEventListener("scroll", function() {
    // Check if the user has scrolled to a certain extent
    if (window.scrollY > 400) {
      // If so, set the display property of the button to "block"
      button.style.display = "block";
     
    } else {
      // Otherwise, set the display property of the button to "none"
      button.style.display = "none";
    }


    if (this.window.scrollY >100) {

      logoTitle.style.display ="block";
    }
    else {
      logoTitle.style.display ="none";
    }
    
  });
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 16
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */

  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
       
        selectHeader.classList.add('header-scrolled')
       
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Initiate glightbox 
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });

      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

})()


const cookieAlert = document.getElementById("cookie-alert");
const acceptCookiesButton = document.getElementById("accept-cookies");
const rejectCookiesButton = document.getElementById("reject-cookies");

// Check if the user has already accepted or rejected cookies
if (localStorage.getItem("cookiesAccepted")) {
  cookieAlert.style.display = "none";
} else if (localStorage.getItem("cookiesRejected")) {
  // If the user has already rejected cookies, hide the alert and don't show it again
  cookieAlert.style.display = "none";
} else {
  // If the user hasn't accepted or rejected cookies, show the alert
  cookieAlert.style.display = "block";
}

// Add an event listener to the accept cookies button
acceptCookiesButton.addEventListener("click", () => {
  // Set a cookie to remember that the user has accepted cookies
  localStorage.setItem("cookiesAccepted", true);
  // Hide the cookie alert
  cookieAlert.style.display = "none";
});

// Add an event listener to the reject cookies button
rejectCookiesButton.addEventListener("click", () => {
  // Set a cookie to remember that the user has rejected cookies
  localStorage.setItem("cookiesRejected", true);
  // Hide the cookie alert
  cookieAlert.style.display = "none";
});





const form = document.querySelector('form');
const submitButton = form.querySelector('input[type="submit"]');

const fullName = form.querySelector('#full-name');
const companyName = form.querySelector('#company-name');
const emailAddress = form.querySelector('#email-address');
const mobileNumber = form.querySelector('#mobile-number');
const pickUpLocation = form.querySelector('#pick-up-location');
const deliveryDestination = form.querySelector('#delivery-destination');
const vehicleType = form.querySelector('#vehicle-type');
const cargoType = form.querySelector('#cargo-type');
const cargoWeight = form.querySelector('#cargo-weight');
const cargoVolume = form.querySelector('#cargo-volume');

const offerAmount = form.querySelector('#offer-amount');
const fullNameError = form.querySelector('#full-name-error');
const companyNameError = form.querySelector('#company-name-error');
const emailAddressError = form.querySelector('#email-address-error');
const mobileNumberError = form.querySelector('#mobile-number-error');
const pickUpLocationError = form.querySelector('#pick-up-location-error');
const deliveryDestinationError = form.querySelector('#delivery-destination-error');
const vehicleTypeError = form.querySelector('#vehicle-type-error');
const cargoTypeError = form.querySelector('#cargo-type-error');
const cargoWeightError = form.querySelector('#cargo-weight-error');
const cargoVolumeError = form.querySelector('#cargo-volume-error');

const offerAmountError = form.querySelector('#offer-amount-error');

submitButton.addEventListener('click', function(event) {
  event.preventDefault();
  clearErrors();
  if (isFormValid()) {
    form.submit();
  }
});

function isFormValid() {
  let isValid = true;
  if (!fullName.value) {
    fullNameError.innerText = 'Please enter your full name';
    isValid = false;
  }
  if (!companyName.value) {
    companyNameError.innerText = 'Please enter your company name';
    isValid = false;
  }
  if (!emailAddress.value) {
    emailAddressError.innerText = 'Please enter your email address';
    isValid = false;
  } else if (!isValidEmail(emailAddress.value)) {
    emailAddressError.innerText = 'Please enter a valid email address';
    isValid = false;
  }
  if (!mobileNumber.value) {
    mobileNumberError.innerText = 'Please enter your mobile number';
    isValid = false;
  } else if (!isValidMobileNumber(mobileNumber.value)) {
    mobileNumberError.innerText = 'Please enter a valid mobile number';
    isValid = false;
  }
  if (!pickUpLocation.value) {
    pickUpLocationError.innerText = 'Please select a pick up location';
    isValid = false;
  }
  if (!deliveryDestination.value) {
    deliveryDestinationError.innerText = 'Please select a delivery destination';
    isValid = false;
  }
  if (!vehicleType.value) {vehicleTypeError.innerText = 'Please select a vehicle type';
  isValid = false;
  }
  if (!cargoType.value) {
  cargoTypeError.innerText = 'Please enter the cargo type';
  isValid = false;
  }
  if (!cargoWeight.value) {
  cargoWeightError.innerText = 'Please enter the cargo weight';
  isValid = false;
  }
  if (!cargoVolume.value) {
  cargoVolumeError.innerText = 'Please enter the cargo volume';
  isValid = false;
  }
 
  if (!offerAmount.value) {
  offerAmountError.innerText = 'Please enter the offer amount';
  isValid = false;
  }
  return isValid;
  }

  function clearErrors() {
		fullNameError.innerText = '';
		companyNameError.innerText = '';
		emailAddressError.innerText = '';
		mobileNumberError.innerText = '';
		pickUpLocationError.innerText = '';
		deliveryDestinationError.innerText = '';
		vehicleTypeError.innerText = '';
		cargoTypeError.innerText = '';
		cargoWeightError.innerText = '';
		cargoVolumeError.innerText = '';
		capacityError.innerText = '';
		offerAmountError.innerText = '';
	}

	function isValidEmail(email) {
		const emailRegex = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
		return emailRegex.test(email);
	}

	function isValidMobileNumber(mobileNumber) {
		const mobileNumberRegex = /^(\+254|0)\d{9}$/;
		return mobileNumberRegex.test(mobileNumber);
	} 




  function openModal1() {
    document.getElementById("cargo-modal").style.display = "block";
  }
  function openModal2() {
    document.getElementById("passenger-modal").style.display = "block";
  }
  function openModal3() {
    document.getElementById("construction-modal").style.display = "block";
  }

  function openModal4() {
    document.getElementById("register-vehicle-modal").style.display = "block";
  }
  

  function closeModal() {
    document.getElementById("cargo-modal").style.display = "none";
    document.getElementById("passenger-modal").style.display = "none";
    document.getElementById("construction-modal").style.display = "none";
;
  }
  function closeModal4() {
    document.getElementById("register-vehicle-modal").style.display = "none";
  }



const carousel = document.querySelector('.carousel');
const slides = document.querySelector('.slides');
const images = document.querySelectorAll('.slides img');

const slideWidth = images[0].clientWidth;

let currentSlide = 0;
let slideInterval = setInterval(nextSlide, 3000);

// Set the width of the slides container
slides.style.width = `${slideWidth * images.length}px`;

function nextSlide() {
  if (currentSlide === images.length - 1) {
    currentSlide = 0;
  } else {
    currentSlide++;
  }
  slides.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}


const fileUpload = document.getElementById('file-upload');
const successMessage = document.getElementById('success-message');

fileUpload.addEventListener('change', function() {
  const allowedExtensions = /(\.pdf|\.png|\.jpg|\.jpeg)$/i;
  const selectedFile = this.files[0];
  if (!allowedExtensions.exec(selectedFile.name)) {
    alert('Invalid file type. Please select a PDF or image file.');
    this.value = '';
    return;
  }
  successMessage.innerHTML = 'File uploaded successfully.';
});

