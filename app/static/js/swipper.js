const swiper = new Swiper('.swiper', {
  // Optional parameters
  direction: 'horizontal',
  //loop: true,
  slidesPerView: 'auto',
  spaceBetween: 10,
  // If we need pagination
  breakpoints: {
    1600: {
      slidesPerView: 5,
    },
    1136: {
      slidesPerView: 3,
    },
    800: {
      slidesPerView: 2,
    },
    640: {
      slidesPerView: 1,
    },
  },
  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
