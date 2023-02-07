import os

import requests
from dotenv import load_dotenv

GENDER = "non binary"
WEIGHT_KG = 80
HEIGHT_CM = 180
AGE = 18

load_dotenv()  # This reads the environment variables inside .env

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
