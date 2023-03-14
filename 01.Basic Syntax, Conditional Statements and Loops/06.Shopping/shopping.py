budget = int(input())

while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    price = int(command)
    if budget - price < 0:
        print('You went in overdraft!')
        break
    else:
        budget -= price
    





