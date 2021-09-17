number = int(input('Input a number to see if it is a multiple of ten:\n'))

if number < 10:
    print('This number is not a multiple of ten.')

else:
    number = number % 10
    if number == 0:
        print('This value is a multiple of ten.')
    else:
        print('This number is not a multiple of ten.')
