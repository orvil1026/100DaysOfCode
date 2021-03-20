import requests
from decouple import config


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.get_data_endpoint = 'https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/budgetFlightDeals/'
        self.put_data_endpoint = 'https://api.sheety.co/8c2d65f43c36f0cac0717042aac8f1ed/budgetFlightDeals/'
        self.token = config("SHEETY_TOKEN")
        self.sheet_data = None
        self.response = None
        self.header = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

    def get_sheet_data(self, sheetname):
        self.response = requests.get(url=f"{self.get_data_endpoint}/{sheetname}", headers=self.header)
        self.sheet_data = self.response.json()
        return self.sheet_data

    def put_sheet_data(self, json, object_id, sheetname):
        requests.put(url=f'{self.put_data_endpoint}{sheetname}/{object_id}', data=json, headers=self.header)

    def post_sheet_data(self, json, sheetname):
        response = requests.post(url=f"{self.get_data_endpoint}/{sheetname}", json=json, headers=self.header)
        print(response.text)