from itertools import permutations


def not_elementary(num):
    count = 0
    max_number = 0
    numbers = [i for i in str(num)]
    combinations = list(int(''.join(p)) for p in permutations(numbers))

    print(combinations)

    for num in combinations:
        if num % 30 == 0 and num > max_number:
            max_number = num

            count += 1
    if count == 0:
        print(-1)
    else:
        print(max_number)


input_no = int(input())
not_elementary(input_no)
