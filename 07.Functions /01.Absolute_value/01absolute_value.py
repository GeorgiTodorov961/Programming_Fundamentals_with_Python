def absolute(input_data):
    output_list = []
    for number in input_data:
        converted_number = float(number)
        output_list.append(abs(converted_number))
    return output_list


input_line = input().split()
absolute_values = absolute(input_line)

print(absolute_values)

