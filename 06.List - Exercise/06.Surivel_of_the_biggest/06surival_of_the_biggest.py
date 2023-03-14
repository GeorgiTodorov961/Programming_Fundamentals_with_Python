list_of_integers = list(map(int, input().split()))
count = int(input())

for remove in range(count):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)

print(*list_of_integers, sep=", ")

