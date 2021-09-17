sandwich_orders = ['pastrami', 'italian', 'pastrami', 'turkey', 'roast beef', 'ham', 'pastrami']
finished_sandwiches = []

print('Sorry we are currently out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()

    print('I am making you a ' + making_sandwich)
    finished_sandwiches.append(making_sandwich)


for sandwich in finished_sandwiches:
    print(sandwich + ' sandwich is done!')
