def make_album(artist, album, songs = None):
    x = {'Artist': artist, 'Album' : album, 'Number of songs' : songs}
    return x

print(make_album('Renz 1k', 'GVO'))

print(make_album('Babytron', 'Tronalations'))

print(make_album('Kanye', 'ATL'))

print(make_album('Renz 1k', 'GVO', 12))