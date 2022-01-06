sentence = str(input("Enter a sentence to get a count of each word in the given sentence:. "))
word_search = str(input("Enter the word:")).lower()

def word_count(str):
    count = 0

    words = str.split()

    for word in words:

        if word.lower()== word_search :

            count += 1


    return count


print(f"The word {word_search} occurs {word_count(sentence)} times")

