# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# dict_data = data.to_dict()

# get average and max temp

# average_temp = data['temp'].mean()
# max_temp = data['temp'].max()
#
#
# print(average_temp)
# print(max_temp)

# Get columns data
# print(data['temp'])
# print(data.temp)

# Get row data
# print(data[data['day'] == 'Monday'])
# print(data[data['temp'] == data['temp'].max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_in_f = (monday_temp * 1.8) + 32
# print(monday_temp_in_f)

data_dict = {
    'students': ['Orvil', 'Ram', 'James'],
    'marks': [10, 9, 10]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new-data.csv")

