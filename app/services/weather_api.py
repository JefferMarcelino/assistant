import requests
import os 

WEATHER_API = "c8b26af70268b03a95028211abc871d3"

def get_lat_and_lon_by_city_name(city):
  url = f"http://api.openweathermap.org/geo/1.0/direct?q={city.replace(' ', '%20')}&limit=1&appid={WEATHER_API}"

  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      return data[0]
    else:
      return None
  except requests.exceptions.RequestException:
    return None

def get_weather_by_coords(lat, lon):
  url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API}&units=metric"

  try:
    response = requests.get(url)
    if response.status_code == 200:
      weather = response.json()
      return weather
    else:
      return None
  except requests.exceptions.RequestException:
    return None
