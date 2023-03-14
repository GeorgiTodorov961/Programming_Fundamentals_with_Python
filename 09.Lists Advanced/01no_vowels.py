
initial_string = input()

avoid_letters = ['a', 'o', 'u', 'e', 'i']

final_stirng = ''

for letter in initial_string:
    if letter.lower() not in avoid_letters:
        final_stirng += letter

print(final_stirng)
