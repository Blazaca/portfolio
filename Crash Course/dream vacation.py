responses = {}

polling = True

print('This is a poll about your dream vacation spot.')

while polling:
    name = input("What is your name: ")
    response = input("Where would you like to go: ")

    responses[name] = response

    while polling:
        repeat = input('Would you like to add another response?: (y/n)')

        if repeat == 'y':
            break

        elif repeat == 'n':
            polling = False

        else:
            print('Invalid response\n')


for name, location in responses:
    print(name.title() + ' would like to goto ' + location.title() + '!')