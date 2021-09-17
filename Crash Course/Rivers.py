big_rivers = {
    'nile': 'africa',
    'amazon': 'south america',
    'yangtze': 'china',
    'mississippi': 'the united states',
}

for river, area in big_rivers.items():
    print('The ' + river.title() + ' runs through ' + area.title())

for river in big_rivers.keys():
    print(river)

for area in big_rivers.values():
    print(area)


