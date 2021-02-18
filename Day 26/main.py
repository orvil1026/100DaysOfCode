import pandas

# squaring numbers using list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers]
print(squared_numbers)

# filtering even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_num = [n for n in numbers if n % 2 == 0]
print(even_num)

# use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence
# and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()

letters_count = {word: len(word) for word in words}
print(letters_count)

# use Dictionary Comprehension to create a dictionary called weather_f that
# takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)

# iterating over a dataframe

student_data = {
    'name': ['orvil', 'ram', 'sham'],
    'marks': [10, 20, 30]
}
data = pandas.DataFrame(student_data)
print(data)

for (index, row) in data.iterrows():
    print(row['name'])