#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from decouple import config
from pprint import pprint
import requests
from flight_data import FlightData

tequilla_endpoint = 'https://tequila-api.kiwi.com/locations/query'

tequilla_headers = {
    'apikey': config("FLIGHT_API")
}


data = DataManager()
flight_data = FlightData()

sheet_data = data.get_sheet_data()['prices']

for city in sheet_data:

    flight_data.get_flight_data(city['iataCode'],city['city'])

    # parameters = {
    #     'term': city['city']
    # }
    # response = requests.get(url=tequilla_endpoint, params=parameters, headers=tequilla_headers)
    # iata_code = response.json()['locations'][0]['code']
    # data_json = {
    #     "price": {
    #         "city": city['city'],
    #         "iataCode": iata_code,
    #         "lowestPrice": city['lowestPrice']
    #     }
    # }
    # response = requests.put(url=f'https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/budgetFlightDeals/prices/{city["id"]}',json=data_json,headers=data.header)
    # data.put_data_endpoint(json, city['id'])

# pprint(sheet_data)

