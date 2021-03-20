#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from decouple import config
from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch
import pprint

tequilla_endpoint = 'https://tequila-api.kiwi.com/locations/query'

tequilla_headers = {
    'apikey': config("FLIGHT_API")
}


data = DataManager()

flight_search = FlightSearch()

sheet_data = data.get_sheet_data('prices')['prices']

# Get users

print("Welcome to the Flight Club!\n We find the best deals and email you .")
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
email = input("Enter your email id:")

# get email data
email_data = data.get_sheet_data('users')['users']
email_list = []
for email in email_data:
    email_list.append(email['email'])

print(email_list)

json = {
    "user": {
        "firstname": first_name,
        "lastname": last_name,
        "email": email,

    }
}
data.post_sheet_data(json, 'users')


for city in sheet_data:

    iataCode = city['iataCode']
    flight_data = flight_search.get_flight_data(fly_to=iataCode)

    # flight_data = FlightData(response)
    if flight_data.price <= city['lowestPrice']:
        notify = NotificationManager()
        for email in email_list:
            mail = notify.send_mail(email,flight_data)


