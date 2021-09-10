states = ['California', 'Washington', 'Pennsylvania', 'Alaska', 'Texas']
print(states)

states.append('Alabama')
print(states)

states.insert(2, 'Oregon')
print(states)

del states[-1]
print(states)

removed_states = [states.pop()]
for state in removed_states:
    print(state + ' is officially uninvited from the country')

states.insert(3, 'New York')
print(sorted(states))
print(sorted(states, reverse=True))

states.sort()
print(states)
states.sort(reverse=True)
print(states)



