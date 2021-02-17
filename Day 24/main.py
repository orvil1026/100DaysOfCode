# file = open("my-file.txt")
# context = file.read()
# print(context)
# file.close()


with open("../../../Desktop/my-file.txt", mode='r') as file:
    context = file.read()
    # file.write("\nHello my name is Orvil D'silva . \n #100DaysOfCode")
    print(context)
