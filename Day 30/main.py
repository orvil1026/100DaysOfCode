# try:
#     file = open('new_file.txt')
#     a_dictionary = {'key':'value'}
#     # a_dictionary['ss']
#
# except FileNotFoundError:
#     file = open('new_file.txt', mode='w')
#     file.write("something")
#
# except KeyError as error_message:
#     print(f'the Key {error_message} does not exist')
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     raise KeyError

# height = int(input("Enter your height"))
# weight = int(input("ENter your weight"))
#
# if height > 3:
#     raise ValueError("Height should not be over 3m.")
#
# bmi = weight / height ** 2
# print(bmi)


# 30.1
fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
#
#
# make_pie(4)

# 30.2

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        post_likes = post['Likes']
    except KeyError:
        post_likes = 0
    finally:
        total_likes = total_likes + post_likes


print(total_likes)