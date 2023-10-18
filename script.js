function isElementInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
function animateTimeline() {
    const sections = document.querySelectorAll('.row section');

    sections.forEach((section) => {
        if (isElementInViewport(section)) {
            section.classList.add('slide-in');
        }
    });
}
animateTimeline();
window.addEventListener('scroll', animateTimeline);

