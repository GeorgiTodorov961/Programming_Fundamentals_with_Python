sentence = input().split()
new_list = [word for word in sentence if len(word) % 2 == 0]
print('\n'.join(word for word in new_list))
