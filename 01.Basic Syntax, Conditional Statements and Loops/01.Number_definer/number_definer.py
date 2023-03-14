input_number = float(input())

if input_number > 0:
    if input_number < 1:
        print('small positive')
    elif input_number > 1000000:
        print('large positive')
    else:
        print('positive')
elif input_number < 0:
    if input_number > -1:
        print('small negative')
    elif input_number < -1000000:
        print('large negative')
    else:
        print('negative')
else:
    print('zero')
    



