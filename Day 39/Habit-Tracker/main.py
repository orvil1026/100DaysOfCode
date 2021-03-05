import requests

from datetime import datetime

TOKEN = 'hdhdhdkdaldkjdfkjsdf'
GRAPH_ID = 'habit1'
pixela_endpoint = 'https://pixe.la/v1/users'

parameters = {
    'token': TOKEN,
    'username': 'orvil1026',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=parameters)

graph_endpoint = f'{pixela_endpoint}/orvil1026/graphs'

graph_summary = {
    'id': GRAPH_ID,
    'name': 'Coding',
    'unit': 'hours',
    'type': 'int',
    'color': 'kuro',

}

headers = {
    "X-USER-TOKEN": TOKEN,

}


# response = requests.post(url=graph_endpoint, json=graph_summary, headers=headers)
#
# print(response.text)


yyyyMMdd = datetime.today().strftime('%Y%m%d')

add_pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

pixel_parameters = {
    'date': '20210303',
    'quantity': '5'

}
update_pixel_endpoint = f'{add_pixel_endpoint}/20210303'

update_pixel = {
    'quantity': '0'
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers)

print(response.text)