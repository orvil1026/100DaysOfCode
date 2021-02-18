import pandas

# TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_dict ={row['letter']: row['code'] for (index,row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter the word:").upper()

result = [letter_dict[letter] for letter in user_input]
print(result)