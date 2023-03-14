def perfect_number(some_number):
    aliquot_sum = sum([num for num in range(1, (some_number // 2) + 1) if some_number % num == 0])
    if aliquot_sum == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

perfection = perfect_number(number)

print(perfection)


