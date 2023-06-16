import requests

def get_advice():
  url = "https://api.adviceslip.com/advice"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      return data["slip"]["advice"]
    else:
      return "Advice not available"
  except requests.exceptions.RequestException:
    return "Failed to fetch advice"
