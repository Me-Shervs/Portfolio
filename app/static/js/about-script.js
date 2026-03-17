document.addEventListener("DOMContentLoaded", function () {
    // Carousel
    let next = document.querySelector('.next');
    let prev = document.querySelector('.prev');
    let slide = document.querySelector('.slide');

    if (next && prev && slide) {
        next.addEventListener('click', function () {
            let items = document.querySelectorAll('.item');
            slide.appendChild(items[0]);
        });

        prev.addEventListener('click', function () {
            let items = document.querySelectorAll('.item');
            slide.insertBefore(items[items.length - 1], items[0]);
        });
    }
});