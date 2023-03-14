factor = int(input())
count = int(input())

numbers_list = []
for number in range(1, count + 1):
    new_number = number * factor
    numbers_list.append(new_number)

print(numbers_list)

