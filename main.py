import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'


# Request body instead of query params
data = {
    "query": input("Tell me which exercises you did: ")
}

x_app_id = os.getenv("x_app_id")
x_app_key = os.getenv("x_app_key")

nutrtion_headers = {
    'Content-Type': 'application/json',
    'x-app-id': x_app_id,
    'x-app-key': x_app_key
}

# Use POST method and send data as JSON
response = requests.post(url=url, json=data, headers=nutrtion_headers)

# Get the response data
response_data = response.json()

#print(response_data)

sheety_url = "https://api.sheety.co/d402550b684693b30dfd589f1de615ff/wrokoutTrackerProject/sheet1"

Authorization = os.getenv("Authorization")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": Authorization
}

for exercise in response_data["exercises"]:
    body = {
        "sheet1":{
            "date":datetime.now().strftime("%d/%m/%Y"),
            "time":datetime.now().strftime("%H:%M:%S"),
            "exercise":exercise["name"],
            "duration":str(exercise["duration_min"]),
            "calories":str(exercise["nf_calories"])
        }
    }

    response = requests.post(url = sheety_url, json=body, headers=sheety_headers)
    print(response.status_code)
    print(response.text)
