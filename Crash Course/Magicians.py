def show_magicians(magicians, great_magicians):
    for magician in magicians:
        print(magician.title())
    for great_magician in great_magicians:
        print(great_magician)


def make_great(magicians):
    while magicians:
        training_magician = str(magicians.pop().title()) + ' the Great'
        great_magicians.append(training_magician)


magicians = ['george', 'anna', 'emily', 'thomas']
great_magicians = []
make_great(magicians[:])
show_magicians(magicians, great_magicians)
