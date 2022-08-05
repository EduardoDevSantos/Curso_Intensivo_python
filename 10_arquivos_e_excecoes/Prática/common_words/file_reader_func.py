def file_reader(*filenames):
    """Ler arquivos de textos"""
    for filename in filenames:
        try:
            with open(filename) as f_obj:
                print(f_obj.read())
        except FileNotFoundError:
            pass

        
file_reader('10_arquivos_e_excecoes/cats.txt',
'10_arquivos_e_excecoes/Prática/cats_dogs/dogs.txt')
