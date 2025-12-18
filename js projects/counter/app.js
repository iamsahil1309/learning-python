const countDisplay = document.getElementById("count");
const decrease = document.getElementById("decrease");
const reset = document.getElementById("reset");
const increase = document.getElementById("increase");

let count = 0;

function updateCount() {
  countDisplay.innerText = count;

  if (count < 0) {
    countDisplay.style.color = "red";
  } else if (count > 0) {
    countDisplay.style.color = "green";
  } else {
    countDisplay.style.color = "black";
  }
}

decrease.addEventListener("click", () => {
    if(count > -10) {
        count--;
        updateCount();
    }
})

increase.addEventListener("click", () => {
    count++
    updateCount()
})

reset.addEventListener("click", () => {
    count = 0
    updateCount()
})

updateCount()