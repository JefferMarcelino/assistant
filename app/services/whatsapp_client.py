import requests
import json
import os 

WA_TOKEN = "EAAFTqn5Jfo4BAOHdNuhgcZBIO2KCRSE82GvWJjsTzMMOvzg2R6X6bk59bKZAQ33khi4vR6zTeBpuOHDMrfGiRZCF4or3f2cDzfPM7wlB5njRcDPHJe8nqvyu0SgMpkvdVDkUL2vSXN9sMPRnUAZCAFAMBkaEgjVraShCNMp5moIE5nas9o0i"

WAID = "105510662311615"

def send_message(number, message):
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {WA_TOKEN}"
  }

  data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "text",
    "text": json.dumps({"body": message})
  }

  response = requests.post(
    f"https://graph.facebook.com/v17.0/{WAID}/messages",
    data=data,
    headers=headers
  )
