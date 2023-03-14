old_version = list(map(int, input().split('.')))
old_version[-1] += 1
for index in range(len(old_version) - 1, -1, -1):
    if old_version[index] > 9:
        old_version[index] = 0
        if index - 1 >= 0:
            old_version[index - 1] += 1


print(*old_version,sep='.')

