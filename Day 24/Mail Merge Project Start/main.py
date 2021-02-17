#TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Getting names list
with open("./Input/Names/invited_names.txt") as names_file:
    names_data = names_file.readlines()

names = []
for name in names_data:
    names.append(name.strip("\n"))

# print(names)

# Getting starting letter

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    # print(starting_letter)


# creating letters
for name in names:

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as letter:
        letter.write(starting_letter.replace("[name]", name))