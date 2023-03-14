numbers_list = list(map(int, input().split(', ')))
print([index for index, number in enumerate(numbers_list) if number % 2 == 0])


