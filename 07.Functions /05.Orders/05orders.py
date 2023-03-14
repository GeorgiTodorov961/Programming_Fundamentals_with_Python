def calculating(input_product, quantity_of_products):
    total_price = 0
    if input_product == 'coffee':
        total_price = quantity_of_products * 1.5
    elif input_product == 'water':
        total_price = quantity_of_products * 1
    elif input_product == 'coke':
        total_price = quantity_of_products * 1.4
    elif input_product == 'snacks':
        total_price = quantity_of_products * 2
    return total_price


product = input()
quantity = int(input())

price = calculating(product, quantity)
print(f'{price:.2f}')
