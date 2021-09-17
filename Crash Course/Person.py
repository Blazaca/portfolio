people = {
    'dphillips': {
        'first_name': 'darby',
        'last_name': 'phillips',
        'age': 24,
        'city': 'denver',
    },
    'fjohnson': {
        'first_name': 'faith',
        'last_name': 'johnson',
        'age': 22,
        'city': 'salt lake city',
    },
    'jupdyke': {
        'first_name': 'jordyn',
        'last_name': 'updyke',
        'age': 23,
        'city': 'portland',
    },
}

for friend, friend_info in people.items():
    full_name = friend_info['first_name'] + " " + friend_info['last_name']
    age = friend_info['age']
    location = friend_info['city']

    print(full_name.title() + " is " + str(age) + ' years old and lives in '
          + location.title())

