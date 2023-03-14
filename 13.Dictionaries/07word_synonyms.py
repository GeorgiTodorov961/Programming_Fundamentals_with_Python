from collections import defaultdict

cycles = int(input())
collection = defaultdict(list)

for number in range(cycles):
    word = input()
    synonym = input()

    collection[word].append(synonym)

for word, synonym_list in collection.items():
    print(f'{word} - {", ".join(syn for syn in synonym_list)}')

