import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])

# squirrel_color = data['Primary Fur Color'].tolist()
# print(squirrel_color)
# squirrel_color_data = {
#     'Cinnamon': 0,
#     'Gray': 0,
#     'Black': 0,
#
# }
#
# for color in squirrel_color:
#     if color == 'Gray' or color == 'Cinnamon' or color == "Black":
#         squirrel_color_data[color] += 1
#
# print(squirrel_color_data)

new_squirrel_data = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey_squirrels, red_squirrels, black_squirrels]
}

new_data = pandas.DataFrame(new_squirrel_data)

new_data.to_csv("new-squirrel.csv")
