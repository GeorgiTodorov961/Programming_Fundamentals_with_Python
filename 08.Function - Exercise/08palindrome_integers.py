def palindrome(numbers):
    palindrom = numbers == numbers[::-1]
    return palindrom


list_of_numbers = list(map(int, input().split(', ')))

for number in list_of_numbers:
    result = palindrome(str(number))
    print(result)


