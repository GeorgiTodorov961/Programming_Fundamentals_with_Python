lines = int(input())

even = True
for _ in range(lines):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        even = False
        break

if even:
    print('All numbers are even.')
    
   




