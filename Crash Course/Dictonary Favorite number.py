people = ['abhi', 'eliana', 'faith', 'georgina', 'bullock']
favorite_numbers = {
    'abhi': 69,
    'eliana': 1111,
    'faith': 2311,
    'georgina': 420,
    'bullock': 123,
}

for person in people:
    print(person.title() + "'s favorite number is " +
            str(favorite_numbers[person]))

