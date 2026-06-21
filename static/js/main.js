/**
 * Super Tasty Cakes Studio — minimal client-side enhancements
 */

document.addEventListener('DOMContentLoaded', function () {
    // Close mobile nav after link click
    const navCollapse = document.getElementById('mainNavbar');
    if (navCollapse) {
        navCollapse.querySelectorAll('.nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                const toggler = document.querySelector('.navbar-toggler');
                if (navCollapse.classList.contains('show') && toggler) {
                    toggler.click();
                }
            });
        });
    }

    // Subtle scroll fade-in for sections below the fold
    if ('IntersectionObserver' in window) {
        const sections = document.querySelectorAll('.section');
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                    entry.target.style.opacity = '1';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.06 });

        sections.forEach(function (section) {
            section.style.opacity = '0';
            observer.observe(section);
        });
    }
});
