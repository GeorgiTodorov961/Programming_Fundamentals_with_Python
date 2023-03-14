from math import factorial


def factorial_number(some_number):
    return factorial(some_number)


def division_of_numbers(number_first, number_second):
    factorial01 = factorial_number(number_first)
    factorial02 = factorial_number(number_second)
    division = factorial01 / factorial02
    return division


first_number = int(input())
second_number = int(input())

result = division_of_numbers(first_number, second_number)

print(f'{result:.2f}')

