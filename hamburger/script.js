const burger = document.getElementById("burger")
const nav = document.querySelector("nav")

burger.addEventListener("click", () => {
  nav.style.transform = "translateX(0px)"
})