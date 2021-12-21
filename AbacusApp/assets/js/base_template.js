const icon = document.querySelector("#icon");
const navbar = document.querySelector(".quick-links");

function condenseSidebar() {
    if (navbar.classList.contains("show")) {
        navbar.classList.remove("show");
    } else{
        navbar.classList.add("show");
    }
}

icon.addEventListener("click",condenseSidebar);