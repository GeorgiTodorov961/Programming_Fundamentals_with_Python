lines = int(input())

initial_list = []

for number in range(lines):
    current_number = int(input())
    initial_list.append(current_number)

command = input()

filtered_number = []
for filter_number in initial_list:
    if command == 'even':
        if filter_number % 2 == 0:
            filtered_number.append(filter_number)
    elif command == 'odd':
        if filter_number % 2 != 0:
            filtered_number.append(filter_number)
    elif command == 'positive':
        if filter_number >= 0:
            filtered_number.append(filter_number)
    elif command == 'negative':
        if filter_number < 0:
            filtered_number.append(filter_number)

print(filtered_number)





