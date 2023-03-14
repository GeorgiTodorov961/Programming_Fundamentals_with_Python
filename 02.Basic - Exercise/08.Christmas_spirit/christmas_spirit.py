quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlant = 3
tree_lights = 15
budget = 0
spirit = 0
for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament_set * quantity
        spirit += 5
    if day % 3 == 0:
        budget += (tree_skirt + tree_garlant) * quantity
        spirit += 3 + 10
    if day % 5 == 0:
        budget += tree_lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += tree_skirt + tree_garlant + tree_lights
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
    


