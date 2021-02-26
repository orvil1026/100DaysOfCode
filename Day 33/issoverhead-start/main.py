import requests
from datetime import datetime
import smtplib

MY_LAT = -2.5713      # 51.507351  Your latitude
MY_LONG = -46.4515      # -0.127758  Your longitude


def is_near():
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_dark():
    return sunset <= current_hour <= sunrise


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

if is_near():

    if is_dark():
        user = '#'
        password = '#'

        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=user, password=password)

        connection.sendmail(
            from_addr=user,
            to_addrs='dsilvaorvil@yahoo.com',
            msg='Subject:ISS Overhead\n\nThe ISS is over head.Get out, and look in the sky.'

        )
        connection.close()








