close_friends = ['Faith', 'Evan', 'Pablo', 'Nick']

# Instead of using print use 'return'


def message_friends(x):
    return close_friends[x] + ' is one of my close friends.'

# Because the def for print(close_friends[x] + 'is one of my close friends.'
# has a second line underneath it print will return the second line as 'none'


print(message_friends(0))
print(message_friends(1))
print(message_friends(2))
print(message_friends(3))


# Modes of transportation
# This method not only saves 4 lines of code
# it's faster :D

transport = ['skateboard', 'snowboard', 'boosted board', 'electric car']

for wheels in transport:
    print('I would like to own a ' + wheels)


# Changing items in lists

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# this line will change an index
motorcycles[0] = 'ducati'

# when changing a list you can change it to a string, var, bool, etc.

# Appending Lists
# appending a list adds another item to the end of the list
# or if the list is empty it will populate

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')
#
# for motorcycle in motorcycles:
#     print(motorcycle)


# Inserting items into a list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycle.insert(0, 'ducati')

# The first variable is the position of insertion
# the second is the item being inserted


