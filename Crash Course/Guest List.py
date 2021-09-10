guests = ['Hannibal Buress', 'Spiderman', 'your mom']

print('We are inviting ' + str(len(guests)) + ' people.')
for guest in guests:
    print("Hello " + guest + "\n You are formally invited to my party!\n")

guests.remove('Spiderman')

print('We are inviting ' + str(len(guests)) + ' people.')
for guest in guests:
    print("Hello " + guest + "\n You are formally invited to my party!\n")

guests.insert(0, 'wanda')
guests.insert(2, 'Aggy')
guests.append('buddy')

print('We are inviting ' + str(len(guests)) + ' people.')
for guest in guests:
    print("Hello " + guest + "\n You are formally invited to my party!\n")

print(guests)

removed_guests = []

for removed_guest in range(3):
    removed_guests.append(guests.pop())

print('We are inviting ' + str(len(guests)) + ' people.')

for removed_guest in removed_guests:
    print("Sorry " + removed_guest + " you are officially uninvited")

for guest in range(2):
    del guests[0]

print(guests)
print(removed_guests)
