// 🔍 Search Filter Function
function filterPackages() {
    let input = document.getElementById("searchBar").value.toLowerCase();
    let cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        let title = card.querySelector("h3").innerText.toLowerCase();
        let description = card.querySelector("p").innerText.toLowerCase();

        if (title.includes(input) || description.includes(input)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}


// 🛒 Book Now Button Function
function bookNow(title) {
    alert("You selected: " + title + " 🌍");

    // 👉 future upgrade: redirect to booking page
    // window.location.href = "/book?package=" + encodeURIComponent(title);
}


// ✨ Optional: Page Load Animation
window.onload = function () {
    let cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        card.style.opacity = 0;
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "all 0.5s ease";
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }, index * 150);
    });
};

function toggleMenu() {
    let menu = document.getElementById("menu");
    menu.classList.toggle("active");
}

