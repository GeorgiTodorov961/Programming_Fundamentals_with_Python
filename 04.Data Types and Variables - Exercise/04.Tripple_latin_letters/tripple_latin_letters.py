input_number = int(input())

start_letter = 97
final_letter = start_letter + input_number

for first in range(start_letter, final_letter):
    for second in range(start_letter, final_letter):
        for thrith in range(start_letter, final_letter):
           print(f"{chr(first)}{chr(second)}{chr(thrith)}")
        


