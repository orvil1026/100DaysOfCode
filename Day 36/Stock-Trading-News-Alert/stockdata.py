import requests
from decouple import config

STOCK = "TSLA"

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': config("STOCK_API_KEY"),

}

response = requests.get("https://www.alphavantage.co/query", params=parameters)

data = response.json()['Time Series (Daily)']
tsla_data = []
for day in data:
    tsla_data = [value for key,value in data.items()]
recent_data = tsla_data[:2]



