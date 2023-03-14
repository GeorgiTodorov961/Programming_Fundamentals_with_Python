lines = int(input())
filter = input()
unfiltered_list = []
filtered_list = []

for string in range(lines):
    current_string = input()
    if filter in current_string:
        filtered_list.append(current_string)
    unfiltered_list.append(current_string)

print(unfiltered_list)
print(filtered_list)

