pets = {
    'sammy': {
        'animal': 'dog',
        'owner': 'blake',
        'size': 'small',
    },
    'wanda': {
        'animal': 'dog',
        'owner': 'faith',
        'size': 'small',
    },
    'streep': {
        'animal': 'cat',
        'owner': 'jordyn',
        'size': 'small',
    }
}

for pet, pet_info in pets.items():
    print(pet.title() + ' is a ' + pet_info['size'] + ' ' + pet_info['animal']
          + '. Their owner is ' + pet_info['owner'].title() + '.')
