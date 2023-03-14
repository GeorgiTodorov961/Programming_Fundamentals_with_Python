lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repairs = lost_fights // 2
sword_repairs = lost_fights // 3
shield_repairs = lost_fights // 6
armor_repairs = shield_repairs // 2

total_helmet_price = helmet_price * helmet_repairs
total_sword_price = sword_price * sword_repairs
total_shield_price = shield_price * shield_repairs
total_armor_price = armor_price * armor_repairs

total_price = total_helmet_price + total_sword_price + total_shield_price + total_armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")
        


