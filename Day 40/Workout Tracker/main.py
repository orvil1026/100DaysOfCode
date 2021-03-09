from decouple import config
import requests
from datetime import datetime

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/homeWorkout/workouts'

exercise = input("what did you do today?")

headers = {
    "x-app-id": config('APP_ID'),
    "x-app-key": config('API_KEY'),

}
parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 167.64,
    "age": 19

}


response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
exercise_data = response.json()['exercises'][0]

# data for sheety params

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.today().strftime("%H:%M")
exercise = exercise_data['user_input']
duration = exercise_data['duration_min']
calories = exercise_data['nf_calories']

# params to be printed in the excel sheet

parameters = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise.title(),
        'duration': duration,
        'calories': calories

    }
}

# headers for sheety api
headers = {
    "Authorization": config("AUTH_TOKEN"),
    "Content-Type": "application/json"
}
print(parameters)

response = requests.post(url=sheety_endpoint, json=parameters, headers=headers)
print(response.text)

