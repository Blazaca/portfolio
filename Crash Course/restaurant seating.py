seats_requested = int(input('How many seats would you like to request?\n'))

if seats_requested >= 8:
    print('We currently have no seats available. You must wait.')
else:
    print("You're table is ready!")

