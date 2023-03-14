group_size = int(input())
days = int(input())

coins = 0

for today in range(1, days + 1):
    coins += 50
    if today % 10 == 0:
        group_size -= 2
    if today % 15 == 0:
        group_size += 5
    coins -= 2 * group_size
    if today % 3 == 0:
        coins -= 3 * group_size
    if today % 5 == 0:
        coins += 20 * group_size
        if today % 3 == 0:
            coins -= 2 * group_size

average_coins = int(coins / group_size)
print(f'{group_size} companions received {average_coins} coins each.')

        


6