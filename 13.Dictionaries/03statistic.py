storage = {}

while True:
    command = input()
    if command == 'statistics':
        break

    product, quantity = command.split(': ')
    if product not in storage:
        storage[product] = 0
    storage[product] += int(quantity)

print("Products in stock:")
for product, quantity in storage.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(storage.keys())}')
print(f'Total Quantity: {sum(storage.values())}')



