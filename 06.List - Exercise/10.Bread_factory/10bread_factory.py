day_events = input().split('|')

total_energy = 100
total_coins = 100

handle_event = True

for event in day_events:
    input_data = event.split('-')
    command = input_data[0]
    number = int(input_data[1])

    if command == 'rest':
        current_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif command == 'order':
        if total_energy - 30 >= 0:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins - number >= 0:
            total_coins -= number
            print(f"You bought {command}.")
        else:
            handle_event = False
            print(f"Closed! Cannot afford {command}.")
            break

if handle_event:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
