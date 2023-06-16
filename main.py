from app.services.notification_service import NotificationService

def main():
  # Instantiate the NotificationService
  notification_service = NotificationService()

  # Example usage
  number = "+258843997730"
  city = "Mavalane A"

  notification_service.send_text_notification(number, "Good Morning Jeffer!")
  notification_service.send_advice_notification(number)
  notification_service.send_weather_notification(number, city)

if __name__ == '__main__':
  main()
