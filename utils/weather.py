import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# ---------- Get coordinates for ANY city ----------
def get_city_coordinates(city):
    geo_url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }

    response = requests.get(geo_url, params=params)
    data = response.json()

    if not data:
        return None

    return data[0]["lat"], data[0]["lon"]

# ---------- Get live weather using coordinates ----------
def get_current_weather(city):
    if not API_KEY:
        return None

    coords = get_city_coordinates(city)
    if not coords:
        return None

    lat, lon = coords

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(weather_url, params=params)
    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "city": city.title(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "weather": data["weather"][0]["description"]
    }
