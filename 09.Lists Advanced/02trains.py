wagon_number = [0 for i in range(int(input()))]

while True:
    command = input()
    if command == 'End':
        print(wagon_number)
        break

    input_data = command.split()
    order = input_data[0]
    index = int(input_data[1])

    if order == 'add':
        people = index
        wagon_number[-1] += people
    elif order == 'insert':
        people = int(input_data[2])
        wagon_number[index] += people
    elif order == 'leave':
        people = int(input_data[2])
        wagon_number[index] -= people

