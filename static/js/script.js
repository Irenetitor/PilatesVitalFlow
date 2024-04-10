// Enabling/Disabling answers and changing background for faq items 

var ques = document.getElementsByClassName("question");
var i = 0;
for (i = 0; i < ques.length; i++) {
    console.log(ques[i])

    ques[i].addEventListener("click", function() {
        console.log("click")
        console.log(this.nextElementSibling)

        this.classList.toggle("active")

        var answer = this.nextElementSibling;
        if (answer.style.display === "block") {
            answer.style.display = "none";
        } else {
            answer.style.display = "block";
        }

    })
}