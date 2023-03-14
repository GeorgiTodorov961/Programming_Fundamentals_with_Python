sequence_of_numbers = list(map(int, input().split(', ')))

group = 10

while len(sequence_of_numbers) > 0:
    current_group = [num for num in sequence_of_numbers if num <= group]
    for number in current_group:
        if number in sequence_of_numbers:
            sequence_of_numbers.remove(number)
    print(f"Group of {group}'s: {current_group}")
    group += 10
