const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".header nav a");
let menuIcon = document.querySelector("#menu-icon");
let navbarlinks = document.querySelector(".navbar");

function handleScroll() {
  const currentScrollPos = window.pageYOffset;

  sections.forEach((section) => {
    const sectionTop = section.offsetTop - 150;
    const sectionBottom = sectionTop + section.offsetHeight;

    if (currentScrollPos >= sectionTop && currentScrollPos <= sectionBottom) {
      const currentSectionId = section.getAttribute("id");
      navLinks.forEach((navLink) => {
        if (navLink.getAttribute("href").substring(1) === currentSectionId) {
          navLink.classList.add("active");
        } else {
          navLink.classList.remove("active");
        }
      });
    }
  });
  // put a bit bar before menus to make difference
  let header = document.querySelector(".header");
  header.classList.toggle("sticky", window.scrollY > 100);

  menuIcon.classList.remove("bx-x");
  navbarlinks.classList.remove("active"); 

}
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


//password toogle psw and text 
$('#formContact').submit(function (event) {
  event.preventDefault();
  var crsfToken = $('input[name="csrfmiddlewaretoken"]').val()
  var submitButton = $('#submitBtn');
  var formData = {
      email: $('#formContact input[name="email"]').val(),
      name: $('#formContact input[name="name"]').val(),
      content: $('#formContact textarea[name="content"]').val(),
      subject: $('#formContact input[name="subject"]').val(),
  }

  $.ajaxSetup({
      headers: {
          'X-CSRFToken': crsfToken
      }
  })

  // Show loading spinner
  submitButton.find('.fa-spinner').show();
  submitButton.attr('disabled', 'disabled').text('Sending...');

  $.ajax({
      url: 'contact-us/',
      type: 'POST',
      data: formData,
      success: function (response) {
          if (response.message == "success") {
              $('#successModal').modal('show');
              $('#formContact')[0].reset()
          }
      }
      ,
      error: function (xhr, errmsg, err) {
          console.log(xhr.status + ': ' + xhr.responseText)
      },
      complete: function () {
          // Hide loading spinner, enable submit button, and revert text
          submitButton.find('.fa-spinner').hide();
          submitButton.removeAttr('disabled').text('Send Message');
      }
  })
})


