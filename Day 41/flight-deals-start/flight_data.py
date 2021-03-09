from decouple import config
import requests
import datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.depature_city = 'LON'
        self.today = datetime.datetime.now()
        self.date_to = datetime.datetime.now() + datetime.timedelta(days=30*6)
        self.return_from = datetime.datetime.now() + datetime.timedelta(days=7)
        self.return_to = datetime.datetime.now() + datetime.timedelta(days=28)
        self.parameters = None
        self.headers = {
            'apikey': config('FLIGHT_API')
        }
        self.search_endpoint = 'https://tequila-api.kiwi.com/v2/search'



    def get_flight_data(self,fly_to,city):

        self.parameters = {
            'fly_from': self.depature_city,
            'fly_to': fly_to,
            'date_from': self.today.strftime('%d/%m/%Y'),
            'date_to': self.date_to.strftime('%d/%m/%Y'),
            'return_from': self.return_from.strftime('%d/%m/%Y'),
            'return_to': self.return_to.strftime('%d/%m/%Y'),
            'curr': 'GBP'



        }
        response = requests.get(url=self.search_endpoint, params=self.parameters, headers=self.headers)
        print(city,f"£{response.json()['data'][0]['price']}")
