
n1 = int(input("Enter the first no:"))
n2 = int(input("Enter the second no:"))
n3 = int(input("Enter the third no:"))

if n1 > n2 and n1 > n3:
    large = n1
elif n2 > n3:
    large = n2
else:
    large = n3

print(f'The Largest number is {large}')

