def sandwich_topper(*sandwich_toppings):
    print('This sandwich has: ')
    for topping in sandwich_toppings:
        print(topping)


sandwich_topper('tomatoes', 'onions', 'turkey')
sandwich_topper('bacon', 'mayo')
sandwich_topper('Alfredo sauce', 'jerk chicken', 'roast beef', 'lemons')