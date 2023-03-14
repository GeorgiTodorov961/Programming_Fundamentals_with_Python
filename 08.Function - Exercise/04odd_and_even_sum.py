def odd_sum(num):
    odd_number = sum([int(odd) for odd in num if int(odd) % 2 != 0])
    return odd_number


def even_sum(num):
    even_number = sum([int(even) for even in num if int(even) % 2 == 0])
    return even_number

number = input()

sum_of_odd_digits = odd_sum(number)
sum_of_even_digits = even_sum(number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")


