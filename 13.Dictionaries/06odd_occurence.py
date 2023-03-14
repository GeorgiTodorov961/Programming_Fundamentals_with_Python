from collections import defaultdict

line = input().split()
collect = defaultdict(int)

for element in line:
    collect[element.lower()] += 1

print(' '.join(key for key, value in collect.items() if value % 2 != 0))

