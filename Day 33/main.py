import requests
import datetime as dt

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# print(latitude, longitude)

MY_LAT = 19.075983
MY_LON = 72.877655

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0

}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise, sunset)
now = dt.datetime.now()
hour = now.hour
print(hour)