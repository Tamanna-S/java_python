import requests
from datetime import datetime
import sys

GENDER = "female"
WEIGHT_KG = 48
HEIGHT_CM = 170
AGE = 15

APP_ID = "821b781f" 
API_KEY = "8d4dd5bce67a4edd23d81826c1a8e844"

exercize_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercize_text = input("tell me which exersize u did : ")

headers = {
    "x-app-id" :APP_ID,
    "x-app-key" :API_KEY
}

parameters = {
    "query" : exercize_text,
    "gender" : GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercize_endpoint, json= parameters, headers= headers)

result = response.json()


post_api = "https://api.sheety.co/340901e51ddc58930c91a4d2b7f54662/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date" :today_date,
            "time" : now_time,
            "exercise" : exercise["name"],
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }
    

#or
# sheet_inputs = {
#     "workout":{
#         "date" :today_date,
#         "time" : now_time,
#         "exercise" : result["exercises"][0]["name"],
#         "duration" : result["exercises"][0]["duration_min"],
#         "calories" : result["exercises"][0]["nf_calories"]
#     }
# }                                 #these both give the same sheet_inputs

headers2 = {"Authorization": "Bearer sahimainbhotmaarungi"}

sheet_response = requests.post(post_api, json=sheet_inputs, headers= headers2)

print(sheet_response.text)



