substrings = input().split(', ')
words = input().split(', ')

occurrences = []

for substring in substrings:
    for word in words:
        if substring in word and substring not in occurrences:
            occurrences.append(substring)

print(occurrences)

