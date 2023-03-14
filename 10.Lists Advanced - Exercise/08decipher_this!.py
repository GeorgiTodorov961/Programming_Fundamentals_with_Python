message = input().split()

reveal = []

for word in message:
    number_as_string = ''
    current_word = []
    for symbol in word:
        if symbol.isdigit():
            number_as_string += symbol
        else:
            current_word.append(symbol)
    number_as_digits = int(number_as_string)
    current_word.insert(0, chr(number_as_digits))
    if len(current_word) > 2:
        current_word[1], current_word[-1] = current_word[-1], current_word[1]
    reveal.append(''.join(current_word))

print(*reveal)


