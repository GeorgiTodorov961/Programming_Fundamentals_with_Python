snowballs_quantity = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for snowball in range(1, snowballs_quantity + 1):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > best_value:
        best_weight = current_weight
        best_time = current_time
        best_quality = current_quality
        best_value = current_value

print(f"{best_weight} : {best_time} = {best_value:.0f} ({best_quality})")
        



