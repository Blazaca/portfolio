track_list = ['wacko', 'musty', 'ooop', 'vestabul', 'trash', 'headrush', 'LYK']
banned_tracks = ['wacko', 'vestabul']
deluxe_tracks = ['headrush', 'trash']
banned_areas = ['america', 'china']
user_location = 'canada'

print('These tracks are currently available in your area: ')
for track in track_list:
    if user_location not in banned_areas:
        if track not in banned_tracks:
            if track not in deluxe_tracks:
                print(track.title())

print("\nThese tracks are available in the Deluxe Edition: ")
for track in deluxe_tracks:
    print(track.title())

request_1 = 'wacko'
print("\nIs the track Wacko on the list?")
if request_1 in track_list:
    print("Yes! Wacko is on the list!")

print('\nIs the album shorter than 3 songs?')
if len(track_list) <= 3:
    print("Yes the album is shorter than 3 songs.")
else:
    print('No the album is ' + str(len(track_list)) + ' songs long.')

print("\nIs Dumbo on the list?")
if 'dumbo' not in track_list:
    print("No that is not on the list.")
else:
    print("Yes it is on the list!")
