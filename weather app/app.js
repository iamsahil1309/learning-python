const city = document.getElementById("city")
const search = document.getElementById("searchBtn")
const tempEl = document.getElementById("temp");
const descEl = document.getElementById("desc");
const humEl = document.getElementById("hum");
const windEl = document.getElementById("wind");
const feelsEl = document.getElementById("feels");
const timeEl = document.getElementById("time");
const dateEl = document.getElementById("date");
const statusEl = document.getElementById("status");
const sunEl = document.getElementById("sun");
const cloudEl = document.getElementById("cloud");


let id = "d19fef121990e40610dd36d828cc9eac";

async function getData() {
  let cityName = city.value

  const url =
    `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${id}`;

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error("HTTP error: " + response.status);
    }

    const data = await response.json();
    console.log(data);
    updateUI(data)
    city.value = "";

  } catch (error) {
    console.error("Error:", error);
  }
}


search.addEventListener("click", getData)

function updateIcon(weather) {
  // Hide all first
  sunEl.style.display = "none";
  cloudEl.style.display = "none";

  switch (weather) {
    case "Clear":
      sunEl.style.display = "block";
      break;

    case "Clouds":
      cloudEl.style.display = "block";
      break;

    case "Rain":
    case "Drizzle":
    case "Thunderstorm":
      cloudEl.style.display = "block";
      cloudEl.classList.add("rain");
      break;

    case "Mist":
    case "Haze":
    case "Fog":
      cloudEl.style.display = "block";
      break;

    default:
      cloudEl.style.display = "block";
  }
}


function updateUI(data) {
  tempEl.innerHTML = `${Math.round(
    data.main.temp
  )}<span class="temp-unit">°C</span>`;
  descEl.textContent = data.weather[0].description;

  humEl.textContent = `${data.main.humidity}%`;
  windEl.textContent = `${data.wind.speed} m/s`;
  feelsEl.textContent = `${Math.round(data.main.feels_like)}°C`;

  
  updateIcon(data.weather[0].main);
  updateDateTime();
}

function updateDateTime() {
  const now = new Date();

  timeEl.textContent = now.toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });

  dateEl.textContent = now.toLocaleDateString([], {
    weekday: "short",
    day: "numeric",
    month: "short",
  });
}
