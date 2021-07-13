import requests
from datetime import *

LOCATION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/b755188ae7d54bb8e8082a67e3f21400/copyOfMyWorkouts/workouts"
APP_ID = "0c606285"
APP_KEY = "c52b4a6651ad4cdb2a352e1bd48c4f3b"
AUTHORIZATION = "Basic ZGF5X2RyZWFtZXI6QWRtaW5AMTIz"

HEADER = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY
}

PARAMETERS = {
    "query" : input("Enter your query"),
    "gender" : input("Are you male or female"),
    "weight_kg" : input("Enter your weight"),
    "height_cm" : input("Enter height"),
    "age" : input("Enter age")
}

response = requests.post(url = LOCATION_ENDPOINT, json = PARAMETERS, headers = HEADER)
data = (response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    header = {
       "Authorization" : AUTHORIZATION
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=header)
