def smallest(one, two, three):
    min_number = [one, two, three]
    return min(min_number)


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = smallest(first_number, second_number, third_number)

print(result)

