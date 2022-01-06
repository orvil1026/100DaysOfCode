
file = open('hello.txt', mode='a')

file.write(' Orvil')

file.close()

file = open('hello.txt')
text = file.read()
print(text)