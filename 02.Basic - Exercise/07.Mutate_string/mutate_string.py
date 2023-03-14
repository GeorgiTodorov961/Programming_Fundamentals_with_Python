first_string = input()
second_string = input()

last_string = first_string
for index in range(len(first_string)):
    right_part = first_string[index + 1::]
    left_part = second_string[:index + 1:]
    current_strign = left_part + right_part
    if current_strign != last_string:
        print(current_strign)
        last_string = current_strign
    


