data = input().split()
searched_food = input().split()
food_dict = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])
    food_dict[product] = quantity


for product in searched_food:
    if product in food_dict.keys():
        print(f"We have {food_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


