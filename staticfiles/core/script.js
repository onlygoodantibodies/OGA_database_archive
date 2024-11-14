// JavaScript to toggle the hamburger menu
document.querySelector('.hamburger').addEventListener('click', function () {
    const menu = document.querySelector('nav ul');
    menu.classList.toggle('show'); // Toggle the 'show' class
});

// Optional: Close the menu when clicking anywhere outside the menu
document.addEventListener('click', function (event) {
    const menu = document.querySelector('nav ul');
    const hamburger = document.querySelector('.hamburger');
    
    if (!menu.contains(event.target) && !hamburger.contains(event.target)) {
        menu.classList.remove('show'); // Hide the menu if clicked outside
    }
});

// Optional: Close the menu when clicking a menu link
document.querySelectorAll('nav ul li a').forEach(function (link) {
    link.addEventListener('click', function () {
        document.querySelector('nav ul').classList.remove('show'); // Close menu
    });
});
