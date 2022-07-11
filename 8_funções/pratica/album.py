def make_album(artname,talbum,nfaixas=''):
    album = {'artista':artname,'titulo':talbum}
    if nfaixas:
        album['faixas'] = nfaixas
    return album
artist = make_album('Shawn Mendes','illuminate','15')
print(artist)
artist = make_album('Ed Sheeran','÷')
print(artist)
artist = make_album('James Arthur','Back from the Edge','11')
print(artist)