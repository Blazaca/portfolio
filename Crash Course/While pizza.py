flag = True
print('What would you like on your pizza? \nType "quit" to stop')
while flag:
    topping = input('Enter a pizza a topping to add!')

    if topping.lower() == 'quit':
        flag = False

    elif topping == '':
        print('Invalid input.')

    else:
        print('Adding ' + topping + ' to the pizza...\n')
