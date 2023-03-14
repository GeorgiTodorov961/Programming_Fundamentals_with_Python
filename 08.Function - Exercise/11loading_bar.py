def loading_bar(some_number):
    if some_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    return f'{some_number}% [{"%" * (some_number // 10) + "." * (10 - (some_number // 10))}]' \
           f'\nStill loading...'


number = int(input())
result = loading_bar(number)
print(result)

