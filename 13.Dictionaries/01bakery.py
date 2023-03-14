input_line = input().split(' ')
food_dict = {}

for index in range(0, len(input_line), 2):
    food = input_line[index]
    quantity = input_line[index + 1]
    food_dict[food] = int(quantity)

print(food_dict)
