from app.services.whatsapp_client import send_message
from app.services.weather_api import get_lat_and_lon_by_city_name, get_weather_by_coords
from app.services.advice_api import get_advice

class NotificationService:
  def __init__(self):
    pass

  def send_weather_notification(self, number, city):
    location = get_lat_and_lon_by_city_name(city)
    if location:
      weather = get_weather_by_coords(location["lat"], location["lon"])
      if weather:
        weather_info = f"*{weather['city']['country']} - {weather['city']['name']}*\n\nGeographic coordinates\n*Longitude:* {weather['city']['coord']['lon']}\n*Latitude:* {weather['city']['coord']['lat']}\n\n"

        for item in weather['list'][:10]:
          weather_info += f"{item['dt_txt']}\n{(item['weather'][0]['description']).capitalize()}\n*Temperature:* {item['main']['temp']}ºC\n*Rain:* {round(item['pop'] * 100)}%\n*Humidity:* {item['main']['humidity']}%\n*Wind:* {item['wind']['speed']}m/s\n\n\n"

        send_message(number, weather_info)
      else:
        send_message(number, "Weather information not available")
    else:
      send_message(number, "City not found")

  def send_advice_notification(self, number):
    advice = get_advice()
    send_message(number, advice)

  def send_text_notification(self, number, message):
    send_message(number, message)
