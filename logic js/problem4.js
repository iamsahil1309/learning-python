function sumOfDigit(num) {
    
    let str = num.toString().split("")
    let result = 0
    str.forEach(num => {
        result += parseInt(num)
    })
    console.log(result)
}

sumOfDigit(12345)
sumOfDigit("hello")