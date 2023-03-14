people = list(map(int, input().split(', ')))
beggars = int(input())

collected_money = []

beggars_counter = 0

while beggars > beggars_counter:
    current_sum = 0
    for index_of_people in range(beggars_counter, len(people), beggars):
        current_sum += people[index_of_people]
    collected_money.append(current_sum)
    beggars_counter += 1
print(collected_money)

