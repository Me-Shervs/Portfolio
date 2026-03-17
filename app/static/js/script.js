document.addEventListener("DOMContentLoaded", function () {

    let menuIcon = document.querySelector('#menu-icon');
    let navbar = document.querySelector('.navbar');

    if (menuIcon && navbar) {
        menuIcon.onclick = () => {
            menuIcon.classList.toggle('bx-x');
            navbar.classList.toggle('active');
        };
    }

    let sections = document.querySelectorAll('section');
    let navlinks = document.querySelectorAll('header nav a');

    window.onscroll = () => {

        sections.forEach(sec => {
            let top = window.scrollY;
            let offset = sec.offsetTop - 150;
            let height = sec.offsetHeight;
            let id = sec.getAttribute('id');

            if (top >= offset && top < offset + height) {
                navlinks.forEach(link => link.classList.remove('active'));

                let activeLink = document.querySelector('header nav a[href*=' + id + ']');
                if (activeLink) activeLink.classList.add('active');
            }
        });

        let header = document.querySelector('header');
        if (header) {
            header.classList.toggle('sticky', window.scrollY > 100);
        }

        if (menuIcon && navbar) {
            menuIcon.classList.remove('bx-x');
            navbar.classList.remove('active');
        }
    };

    // ScrollReveal (only if loaded)
    if (typeof ScrollReveal !== "undefined") {
        ScrollReveal({
            distance: '80px',
            duration: 2000,
            delay: 200
        });

        ScrollReveal().reveal('.home-content, .heading', { origin: 'top'});
        ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form, .tech-container', { origin: 'bottom'});
        ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left'});
        ScrollReveal().reveal('.home-content p, .about-content', { origin: 'right'});
    }

    // Typed
    if (document.querySelector('.multiple-text') && typeof Typed !== "undefined") {
        new Typed('.multiple-text', {
            strings: ['Programmer', 'Web Developer'],
            typeSpeed: 100,
            backSpeed: 100,
            backDelay: 1000,
            loop: true
        });
    }
});

// Certs & Awards Auto Scroll 

const certScroll = document.querySelector(".cert-scroll");

let scrollAmount = 0;

function autoScroll() {
    scrollAmount += 1;

    if (scrollAmount >= certScroll.scrollWidth - certScroll.clientWidth) {
        scrollAmount = 0;
    }

    certScroll.scrollTo({
        left: scrollAmount,
        behavior: "smooth",
        loop: true,
    });
}

setInterval(autoScroll, 50);