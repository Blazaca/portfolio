bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

# this prints with a capital
print(bicycles[2].title())

# this always prints the last item in a list
# [-2] will give the second to last
# [-3] will give the third to last
# and so on...
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + '.'

print(message)