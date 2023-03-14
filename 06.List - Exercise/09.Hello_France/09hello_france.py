colection_list = input().split('|')
budget = int(input())

ticket_to_france = 150
colected_money = []
for command in colection_list:
    input_command = command.split('->')
    item = input_command[0]
    price = float(input_command[1])

    if item == 'Clothes' and price <= 50:
        if budget - price >= 0:
            budget -= price
            sell_price = price * 1.40
            colected_money.append(sell_price)
    elif item == 'Shoes' and price <= 35:
        if budget - price >= 0:
            budget -= price
            sell_price = price * 1.40
            colected_money.append(sell_price)
    elif item == 'Accessories' and price <= 20.5:
        if budget - price >= 0:
            budget -= price
            sell_price = price * 1.40
            colected_money.append(sell_price)

profit = sum(colected_money) - (sum(colected_money) / 1.4)

print(*[f'{money:.2f}' for money in colected_money])
print(f"Profit: {profit:.2f}")
total_money = sum(colected_money) + budget
if total_money >= ticket_to_france:
    print('Hello, France!')
else:
    print('Not enough money.')
