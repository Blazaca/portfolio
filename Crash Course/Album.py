album_info = {}
enter_album_loop = True


def make_album(artist, album):
    album_info[artist] = album


make_album('james blake', 'overgrown')
make_album('tyler the creator', 'call me if you get lost')
make_album('kanye west', 'donda')

print('Type "q" at anytime to quit.')
print('This is the album log. Here is your currently stored albums: ')
for artist, album in album_info.items():
    print(str(artist.title()) + ' , ' + str(album.title()))

album_entry = True
while album_entry:
    entry_start = input('\nWould you like to add new album entries?\n (y/n):')

    if entry_start == 'y':
        while enter_album_loop:
            artist_input = input('Enter artist name: ')
            if artist_input == 'q':
                quit()
            album_input = input('Enter album name: ')
            if album_input == 'q':
                quit()
            make_album(artist_input, album_input)
            print('This is the new album list:')
            for artist, album in album_info.items():
                print(str(artist.title()) + ' , ' + str(album.title()))

    elif entry_start == 'q' or 'n':
        quit()

