import requests
from decouple import config


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.get_data_endpoint = 'https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/budgetFlightDeals/prices'
        self.put_data_endpoint = 'https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/budgetFlightDeals/prices/'
        self.token = config("SHEETY_TOKEN")
        self.sheet_data = None
        self.response = None
        self.header = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

    def get_sheet_data(self):
        self.response = requests.get(url=self.get_data_endpoint, headers=self.header)
        self.sheet_data = self.response.json()
        return self.sheet_data

    def put_sheet_data(self, json, object_id):
        requests.put(url=f'{self.put_data_endpoint}{object_id}', data=json, headers=self.header)
