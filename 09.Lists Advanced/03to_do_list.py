to_do_list = [0] * 10

command = input()

while command != 'End':
    input_data = command.split('-')
    importance = int(input_data[0]) - 1
    task = input_data[1]
    to_do_list.pop(importance)
    to_do_list.insert(importance, task)
    command = input()

print([to_do for to_do in to_do_list if to_do != 0])


