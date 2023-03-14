unsorted_names = input().split(', ')
sorting = lambda x: (-len(x), x)
print(sorted(unsorted_names, key=sorting))

