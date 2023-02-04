import os

import requests
from dotenv import load_dotenv

load_dotenv()  # This reads the environment variables inside .env
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": "40.9387964",
    "lon": "-74.1351612",
    "units": "metric",
    "exclude": "minutely,daily",
    "appid": WEATHER_TOKEN
}
response = requests.get(WEATHER_URL, params=params)
response.raise_for_status()
hourly_weather = response.json()["hourly"][:12]

will_rain = False

for h_data in hourly_weather:
    w_code = h_data["weather"][0]["id"]
    if int(w_code) < 700:
        # print(w_code)
        will_rain = True
# print(hourly_weather[0]["weather"][0]["id"])

if will_rain:
    print("Umbrella")
