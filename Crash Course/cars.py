def make_car(make, model, **other_info):
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in other_info.items():
        car[key] = value
    return car


car_profile = make_car('subaru', 'outback', color='blue'
                       , tow_package=True, booty_hole=True)

print(car_profile)
