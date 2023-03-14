number_of_refuels = int(input())

pool_fill = 0

for refuel in range(number_of_refuels):
    current_refuel = int(input())
    if pool_fill + current_refuel <= 255:
        pool_fill += current_refuel
    else:
        print("Insufficient capacity!")

print(pool_fill)
        


