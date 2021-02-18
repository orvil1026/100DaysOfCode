# squaring numbers using list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers]
print(squared_numbers)

# filtering even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_num = [n for n in numbers if n % 2 == 0]
print(even_num)