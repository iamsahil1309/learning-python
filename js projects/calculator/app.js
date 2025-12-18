const display = document.getElementById("display")

function appendValue(val) {
    display.value += val
}

function clear () {
    display.value = ""
}

function calculate () {
    display.value = eval(display.value)
}