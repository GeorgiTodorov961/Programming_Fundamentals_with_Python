def calculation(first_side, second_side):
    calculated_area = first_side * second_side
    return calculated_area


side_a = int(input())
side_b = int(input())

area = calculation(side_a, side_b)

print(area)
