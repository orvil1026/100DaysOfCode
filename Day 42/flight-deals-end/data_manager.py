from pprint import pprint
import requests
from decouple import config

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/budgetFlightDeals/prices"
SHEETY_TOKEN = config("SHEETY_TOKEN")


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": SHEETY_TOKEN
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)
