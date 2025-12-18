function randomColor () {
    const random = '0123456789ABCDEF'
    let hex = "#"

    for( let i = 0; i < 6; i++) {
        hex += random[Math.floor(Math.random() * 16)]
    }
    return hex
}

const bgChange = document.getElementById("changeColor")
const code = document.getElementById("colorCode")

bgChange.addEventListener("click", () => {
    const color = randomColor()
    document.body.style.backgroundColor = color
    code.innerText = color
})