favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

attendees = ['jen', 'paul', 'georgina']

for person in attendees:
    if person in favorite_languages.keys():
        print(person.title() + ' Thanks you for taking our poll.')
    else:
        print(person.title() + ' Please take our poll!')
