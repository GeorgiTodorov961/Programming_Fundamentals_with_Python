def add_and_subtract(one, two, three):
    sum_of_numbers = sum_numbers(one, two)
    substract_of_number = subtract(sum_of_numbers, three)
    return substract_of_number


def subtract(sum, three):
    substraction = sum - three
    return substraction


def sum_numbers(one, two):
    sum = one + two
    return sum


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = add_and_subtract(first_number, second_number, third_number)
print(result)

