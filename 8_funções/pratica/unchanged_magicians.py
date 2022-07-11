magicians = ['Houdini','David','Criss','John','Sarah']
magicians_copy = magicians[:]
modified_magicians = []
def show_magicians(magicians):
    """Exibe o nome de todos os mágicos na lista."""
    for magician in magicians:
        print(magician.title())
def make_great(magicians,modified_magicians):
    """Modifica o nome de todos os mágicos da lista."""
    while magicians:
        modified = magicians.pop()
        modified_magicians.append("O grande "+modified)
make_great(magicians_copy,modified_magicians)
show_magicians(modified_magicians)
show_magicians(magicians)
