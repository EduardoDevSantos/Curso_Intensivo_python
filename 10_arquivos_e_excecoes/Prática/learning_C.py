filename = '10_arquivos_e_excecoes/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    string = ''
    for line in lines:
        string+=line
    string = string.replace('python','C')
    print(string)
