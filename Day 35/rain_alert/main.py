import requests
import os
from twilio.rest import Client
from decouple import config

account_sid = config("ACCOUNT_SID")
auth_token = config("AUTH_TOKEN")

api_key = config("OWM_TOKEN")
parameters = {
    'lat': -16.465424,#19.391928,
    'lon': -54.638794,#72.839729,
    'appid': api_key,
    'exclude': 'minutely,daily,alerts,current'

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()

data = response.json()

hourly_data = data['hourly']
twelve_hours = hourly_data[:12]

will_rain = False

for hour in twelve_hours:
    weather_code = hour['weather'][0]['id']
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today! Dont forget to take your umbrella.",
        from_='+16235524092',
        to='+919011189660'
    )
    print(message.status)














