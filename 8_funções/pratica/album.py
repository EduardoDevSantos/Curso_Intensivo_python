def make_album(artname,talbum,nfaixas=''):
    album = {'artista':artname,'titulo':talbum}
    if nfaixas:
        album['faixas'] = nfaixas
    return album
while True:
    print("Entre com ('q') para encerrar o programa.")
    name = input("Qual o nome do artista?: ")
    if name == 'q': break
    title = input("Qual o nome do album?: ")
    if title == 'q':break
    faixas = input("Qual o número de faixas do album?: ")
    if faixas == 'q': break
    result = make_album(name,title,faixas)
    print(result)

