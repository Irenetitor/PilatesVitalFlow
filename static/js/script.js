window.onload = function () {
    console.log("website is loaded!!");
    const header = document.querySelector('header');
    const hamburger_menu_btn = document.querySelector(".hamburger");
    const mobile_nav = document.querySelector(".mobile-nav");

    // Enable/Disable header backgroud 
    window.addEventListener('scroll', function (e) {
        if (window.pageYOffset > 100) {
            header.classList.add('is-scrolling');
        } else {
            header.classList.remove('is-scrolling');
        }
    });

    // Enable/Disable mobile nav menu
    hamburger_menu_btn.addEventListener("click", function () {
        console.log("clicked");
        hamburger_menu_btn.classList.toggle("is-active");
        mobile_nav.classList.toggle("is-active");
    });

    // Function to update the left position
    // Call the function initially and whenever the window is resized
    window.addEventListener('resize', function () {
        const screenWidth = window.innerWidth;
        // Remove classes based on the screen width
        if (screenWidth > 1024) {
            hamburger_menu_btn.classList.remove("is-active");
            mobile_nav.classList.remove("is-active");
        }
    });

    // Enabling/Disabling answers and changing background for faq items 

    var ques = document.getElementsByClassName("question");
    var i = 0;
    for (i = 0; i < ques.length; i++) {
        console.log(ques[i])

        ques[i].addEventListener("click", function () {
            this.firstElementChild.classList.toggle("fa-chevron-down")
            this.firstElementChild.classList.toggle("fa-chevron-up")
            this.classList.toggle("active")

            var answer = this.nextElementSibling;
            if (answer.style.display === "block") {
                answer.style.display = "none";
            } else {
                answer.style.display = "block";
            }
        }
        )
    }
}