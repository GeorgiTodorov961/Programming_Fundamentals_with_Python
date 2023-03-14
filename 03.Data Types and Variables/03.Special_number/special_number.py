input_number = int(input())

searched_sum = [5, 7, 11]

for number in range(1, input_number + 1):
    check_number = str(number)
    special = False
    sum_of_digits = 0
    if len(check_number) < 2:
        sum_of_digits = int(number)
    else:
        first_digit = int(check_number[0])
        second_digit = int(check_number[1])
        sum_of_digits = first_digit + second_digit
    if sum_of_digits in searched_sum:
        special = True
    print(f'{number} -> {special}')
        


