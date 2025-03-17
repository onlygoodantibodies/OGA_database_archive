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

document.addEventListener("DOMContentLoaded", function () {
    const cookieBanner = document.getElementById("cookie-banner");
    const acceptButton = document.getElementById("accept-cookies");
    const rejectButton = document.getElementById("reject-cookies");

    // Check if user already made a choice
    const cookiesAccepted = document.cookie.includes("cookies_accepted=true");

    if (cookiesAccepted || document.cookie.includes("cookies_accepted=false")) {
        cookieBanner.style.display = "none"; // Hide banner if choice was made
    }

// Function to load Google Analytics if cookies are accepted
function loadGoogleAnalytics() {
    // Load the Google Analytics script
    const scriptTag = document.createElement("script");
    scriptTag.async = true;
    scriptTag.src = "https://www.googletagmanager.com/gtag/js?id=G-10W2PEF9SW";
    document.head.appendChild(scriptTag);

    scriptTag.onload = function () {
        // Initialize Google Analytics
        window.dataLayer = window.dataLayer || [];
        function gtag(){ dataLayer.push(arguments); }
        
        gtag('js', new Date());

        // Configure Google Analytics with your Measurement ID
        gtag('config', 'G-10W2PEF9SW', { 'anonymize_ip': true }); // GDPR compliance
    };
}

    // If cookies are already accepted, load Google Analytics
    if (cookiesAccepted) {
        loadGoogleAnalytics();
    }

    // Accept Cookies
    acceptButton.addEventListener("click", function () {
        document.cookie = "cookies_accepted=true; max-age=" + 60 * 60 * 24 * 30 + "; path=/";
        cookieBanner.style.display = "none";
        loadGoogleAnalytics(); // Load Google Analytics immediately without refreshing
    });

    // Reject Cookies
    rejectButton.addEventListener("click", function () {
        document.cookie = "cookies_accepted=false; max-age=" + 60 * 60 * 24 * 30 + "; path=/";
        cookieBanner.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const copyButton = document.getElementById("copy-btn");
    const citationText = document.getElementById("citation-text");

    // Check if elements exist before adding event listeners
    if (!copyButton) {
        console.error("Copy button not found!");
        return;
    }

    if (!citationText) {
        console.error("Citation text not found!");
        return;
    }

    copyButton.addEventListener("click", function () {
        console.log("Citation Text:", citationText.innerText); // Debugging

        if (citationText.innerText.trim() === "") {
            console.error("Citation text is empty!");
            return;
        }

        navigator.clipboard.writeText(citationText.textContent.trim())
            .then(() => {
                alert("Citation copied to clipboard!");
            })
            .catch(err => {
                console.error("Failed to copy: ", err);
            });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const citationText = document.getElementById("citation-text");

    if (!citationText) {
        console.error("Citation text element not found!");
        return;
    }

    console.log("Raw Citation Content:", citationText.innerHTML); // Log the raw HTML content
    console.log("Processed Citation Content:", citationText.innerText.trim()); // Log the processed text
});

