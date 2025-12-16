const cityInput = document.getElementById("city");
const searchBtn = document.getElementById("searchBtn");

const tempEl = document.getElementById("temp");
const descEl = document.getElementById("desc");
const humEl = document.getElementById("hum");
const windEl = document.getElementById("wind");
const feelsEl = document.getElementById("feels");
const timeEl = document.getElementById("time");
const dateEl = document.getElementById("date");
const statusEl = document.getElementById("status");

document.querySelector(".minimal-card").classList.remove("fade");
void document.querySelector(".minimal-card").offsetWidth;
document.querySelector(".minimal-card").classList.add("fade");


let id = "d19fef121990e40610dd36d828cc9eac";

async function getData() {
  const cityName = cityInput.value.trim();
  if (!cityName) return;

  statusEl.textContent = "Loading...";

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${id}`;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("City not found");

    const data = await response.json();

    tempEl.textContent = Math.round(data.main.temp);
    descEl.textContent = data.weather[0].description;
    humEl.textContent = data.main.humidity + "%";
    windEl.textContent = data.wind.speed + " m/s";
    feelsEl.textContent = Math.round(data.main.feels_like) + "°C";

    updateDateTime();
    cityInput.value = "";
    statusEl.textContent = "Updated";
  } catch (err) {
    statusEl.textContent = err.message;
  }
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

searchBtn.addEventListener("click", getData);
