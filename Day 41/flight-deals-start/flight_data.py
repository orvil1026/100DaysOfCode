from decouple import config
import requests
import datetime


class FlightData:

    # This class is responsible for structuring the flight data.
    def __init__(self, response):
        self.price = response['price']
        self.dep_city = response['cityFrom']
        self.arr_city = response['cityTo']
        self.outbound_dt = response['route'][0]['utc_departure'].split('T')[0]
        self.inbound_dt = response['route'][0]['utc_arrival'].split('T')[0]
        self.dept_iata = response['flyFrom']
        self.arr_iata = response['flyTo']

    def display_data(self):
        print(f"price:{self.price} dep_city:{self.dep_city} arr_city:{self.arr_city} \n"
              f"outbound date:{self.outbound_dt} inbound date:{self.inbound_dt}\n"
              f"dept Iata {self.dept_iata} arr Iata {self.arr_iata}")


