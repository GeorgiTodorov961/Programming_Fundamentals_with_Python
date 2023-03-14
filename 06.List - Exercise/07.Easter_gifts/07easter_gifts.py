gifts_list = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    input_data = command.split()
    order = input_data[0]
    gift = input_data[1]
    if order == 'OutOfStock':
        if gift in gifts_list:
            counter = gifts_list.count(gift)
            for count in range(counter):
                index = gifts_list.index(gift)
                gifts_list[index] = 'None'
    elif order == 'Required':
        index_of_gift = int(input_data[2])
        if index_of_gift >= 0 and index_of_gift < len(gifts_list):
            gifts_list[index_of_gift] = gift
    elif order == 'JustInCase':
        gifts_list[-1] = gift

for gift_name in gifts_list:
    if gift_name != 'None':
        print(gift_name, end=' ')

