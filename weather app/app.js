let key = "d19fef121990e40610dd36d828cc9eac";

async function weather(city) {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${key}&units=metric`)
      const data = await response.json()
      console.log(data)
}