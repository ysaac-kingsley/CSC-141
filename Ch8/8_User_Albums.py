def make_album(artist, album, songs = None):
    x = {'Artist': artist, 'Album' : album, 'Number of songs' : songs}
    return x

while True:
    print('Please provide the following information.')
    print('Press q to close the program')

    art_name = input('Type the artists name:')
    if art_name == 'q':
        break

    bum_name = input('Type the album name:')
    if art_name == 'q':
        break
    
    num_song = input('Type the number of songs in the album:')
    if art_name == 'q':
        break

    final = make_album(art_name, bum_name, num_song)
    print(final)