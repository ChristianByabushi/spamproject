const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".header nav a");
let menuIcon = document.querySelector("#menu-icon");
let navbarlinks = document.querySelector(".navbar");

// function handleScroll() {
//   const currentScrollPos = window.pageYOffset;

//   sections.forEach((section) => {
//     const sectionTop = section.offsetTop - 150;
//     const sectionBottom = sectionTop + section.offsetHeight;

//     if (currentScrollPos >= sectionTop && currentScrollPos <= sectionBottom) {
//       const currentSectionId = section.getAttribute("id");
//       navLinks.forEach((navLink) => {
//         if (navLink.getAttribute("href").substring(1) === currentSectionId) {
//           navLink.classList.add("active");
//         } else {
//           navLink.classList.remove("active");
//         }
//       });
//     }
//   });
//   // put a bit bar before menus to make difference
//   let header = document.querySelector(".header");
//   header.classList.toggle("sticky", window.scrollY > 100);

//   menuIcon.classList.remove("bx-x");
//   navbarlinks.classList.remove("active");
// }
// window.addEventListener("scroll", handleScroll);

menuIcon.onclick = () => {
  menuIcon.classList.toggle("bx-x");
  navbarlinks.classList.toggle("active");
};

// when the user click the navbar becomes none and
navLinks.forEach((navLink) => {
  navLink.addEventListener("click", () => {
    menuIcon.classList.toggle("bx-x");
    navbarlinks.classList.toggle("active");
  });
});

// scroll reaveal
ScrollReveal({
  //reset: true,
  distance: "80px",
  duration: 2000,
  delay: 200,
});
ScrollReveal().reveal(".home-content, .heading", { origin: "top" });
ScrollReveal().reveal(".home-img, .contact form", { origin: "bottom" });
ScrollReveal().reveal(".home-content h1, .about-img", { origin: "left" });
ScrollReveal().reveal(".home-content p, .about-content", { origin: "right" });
