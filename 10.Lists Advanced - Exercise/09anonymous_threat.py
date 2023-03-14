def merge(words_list, start, end):
    if start not in range(len(words_list)):
        start = 0
    if end not in range(len(words_list)):
        end = len(words_list)
    merged = [''.join(words_list[start:end + 1])]
    left = words_list[:start]
    right = words_list[end + 1:]
    words_list = left + merged + right
    return words_list


def divide(words_list, index, partition):
    word = words_list.pop(index)
    part = len(word) // partition
    new_parts = []
    start = 0
    end = 0
    for parts in range(partition - 1):
        end += part
        new_parts.append(word[start:end])
        start += part
    new_parts.append(word[end:])
    for idx, wrd in enumerate(new_parts):
        words_list.insert(index + idx, wrd)
    return words_list


initial_line = input().split()

while True:
    command = input()
    if command == '3:1':
        break

    input_data = command.split()
    order = input_data[0]
    start_index = int(input_data[1])
    end_index = int(input_data[2])

    if order == 'merge':
        initial_line = merge(initial_line, start_index, end_index)
    elif order == 'divide':
        initial_line = divide(initial_line, start_index, end_index)

print(*initial_line)


