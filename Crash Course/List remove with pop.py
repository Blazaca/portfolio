# deleting an index using pop()
# The term pop comes from thinking of a
# list as a stack of items and popping one item
# off the top of the stack
# This is a use case where we are taking the last item on the list
# and putting it into the sentence
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned =  motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + '.')

# pop can also be use to take any of the items on the list

first_owned = motorcycles.pop(0)
print("The first motorcycle I've owned is a " + first_owned.title() + '.')

# !!!!!NOTE!!!!!
# pop removes the item from the list but give you control of where it will go
