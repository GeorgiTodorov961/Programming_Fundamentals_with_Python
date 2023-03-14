start = int(input())
end = int(input())

for num in range(end, start, -1):
    if num % start == 0:
        print(num)
        break




