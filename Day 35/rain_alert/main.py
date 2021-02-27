import requests

api_key = "ee9826dea70cf42147b57100f4dc6c6e"
parameters = {
    'lat': 19.391928,
    'lon': 72.839729,
    'appid': api_key,

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()

data = response.json()
print(data['hourly'][0])















