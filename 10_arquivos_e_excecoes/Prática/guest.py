name = input("Digite seu nome: ").title()
filename = '10_arquivos_e_excecoes/names.txt'
with open(filename, 'w') as file_object:
    file_object.write(name+"\n")
