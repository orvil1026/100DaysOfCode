import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_dict ={row['letter']: row['code'] for (index,row) in data.iterrows()}


while True:
    try:
        user_input = input("Enter the word:").upper()
        result = [letter_dict[letter] for letter in user_input]
    except KeyError:
        print("Enter only characters.")
    else:
        print(result)
        break




