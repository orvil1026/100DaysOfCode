import requests
from decouple import config
from flight_data import FlightData
import datetime
import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.depature_city = 'BOM'
        self.today = datetime.datetime.now()
        self.date_to = datetime.datetime.now() + datetime.timedelta(days=30 * 6)
        self.return_from = datetime.datetime.now() + datetime.timedelta(days=7)
        self.return_to = datetime.datetime.now() + datetime.timedelta(days=28)
        self.parameters = None
        self.headers = {
            'apikey': config('FLIGHT_API')
        }
        self.search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
        self.response = None

    def get_flight_data(self, fly_to):
        self.parameters = {
            'fly_from': self.depature_city,
            'fly_to': fly_to,
            'date_from': self.today.strftime('%d/%m/%Y'),
            'date_to': self.date_to.strftime('%d/%m/%Y'),
            'return_from': self.return_from.strftime('%d/%m/%Y'),
            'return_to': self.return_to.strftime('%d/%m/%Y'),
            'curr': 'INR'

        }
        self.response = requests.get(url=self.search_endpoint, params=self.parameters, headers=self.headers)
        try:
            data = self.response.json()['data'][0]
        except IndexError:
            pprint(data)
            print(f"No flights found for {fly_to}")

            return None
        flight_data = FlightData(data)
        print(f"{flight_data.arr_city}:₹{flight_data.price}")
        return flight_data

