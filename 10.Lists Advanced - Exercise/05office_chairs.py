number_of_rooms = int(input())

free_chairs = 0
enough_chairs = True

for room in range(1, number_of_rooms + 1):
    input_data = input().split()
    current_chairs = len(input_data[0])
    visitors = int(input_data[1])
    diff = abs(visitors - current_chairs)
    if visitors > current_chairs:
        print(f'{diff} more chairs needed in room {room}')
        enough_chairs = False
    else:
        free_chairs += diff

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
