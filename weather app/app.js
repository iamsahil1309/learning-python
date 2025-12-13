let id = "d19fef121990e40610dd36d828cc9eac";

let url =
  "https://api.openweathermap.org/data/2.5/weather?units=metric&appid =" + id;

const city = document.getElementById("city");
const search = document.getElementById("searchBtn");

search.addEventListener("click", () => {
  if (city.value != "") {
    searchWeather();
  }
});

const searchWeather = () => {
  fetch(url + "&q=" + city.value)
    .then((res) => res.json())
    .then((data) => {
      console.log(data)
    });
};
