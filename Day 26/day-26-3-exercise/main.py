with open('file1.txt') as file:
    file1_data = file.readlines()
    # file1_num = [int(num.strip('\n')) for num in file1]


with open("file2.txt") as file:
    file2_data = file.readlines()
    # file2_num = [int(num.strip('\n')) for num in file2]

result = [int(num) for num in file1_data if num in file2_data]
# Write your code above 👆

print(result)


