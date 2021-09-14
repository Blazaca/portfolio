pizza_types = ['anchovy', 'pineapple', 'ham', 'cheese']

for pizza in pizza_types:
    print(pizza.title() + ' Pizza')

print("I love pizza!")

pets = ['hamster', 'cat', 'dog', 'rabbit']

for pet in pets:
    print(pet + ' is a four legged creature')

print('These animals are cool!')

friends_pizza = pizza_types[:]
pizza_types.append('sausage')

print('My favorite pizza types are: ')
for pizza in pizza_types:
    print(pizza)
print("My friends favorite pizza types are: ")
for friend_pizza in friends_pizza:
    print(friend_pizza)

