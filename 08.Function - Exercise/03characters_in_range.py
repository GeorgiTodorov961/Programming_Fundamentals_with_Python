def characters(first, second):
    start = ord(first)
    end = ord(second)
    character_list = []
    for num in range(start+1, end):
        character_list.append(chr(num))
    return character_list

first_character = input()
second_character = input()

result = characters(first_character,second_character)

print(*result)


