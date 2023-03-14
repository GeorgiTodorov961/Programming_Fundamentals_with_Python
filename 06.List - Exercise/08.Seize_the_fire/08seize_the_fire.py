fire_cells = input().split('#')
water_level = int(input())

cells_list = []

for cell in fire_cells:
    command = cell.split(' = ')
    type_of_fire = command[0]
    value_of_cell = int(command[1])
    if type_of_fire == 'High':
        if 81 <= value_of_cell <= 125:
            if water_level - value_of_cell >= 0:
                water_level -= value_of_cell
                cells_list.append(value_of_cell)
    elif type_of_fire == 'Medium':
        if 51 <= value_of_cell <= 80:
            if water_level - value_of_cell >= 0:
                water_level -= value_of_cell
                cells_list.append(value_of_cell)
    elif type_of_fire == 'Low':
        if 1 <= value_of_cell <= 50:
            if water_level - value_of_cell >= 0:
                water_level -= value_of_cell
                cells_list.append(value_of_cell)

total_effort = sum(cells_list) * 0.25

print('Cells:')
for fire in cells_list:
    print(f' - {fire}')
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells_list)}")

