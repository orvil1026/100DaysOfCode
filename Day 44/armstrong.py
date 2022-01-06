num=int(input("Enter a number to check it is an Armstrong number or not? "))

temp = num

sum = 0

power = len(str(num))

while temp > 0:

    digit = temp % 10

    sum = sum + digit ** power

    temp = temp // 10

if num == sum:

    print(num," is Armstrong number.")

else:

    print(num," is not a Armstrong number.")