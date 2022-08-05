filename = '10_arquivos_e_excecoes/learning_python.txt'
with open(filename) as file_object:
    text = file_object.read()
    print(text+"\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
    print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string+=line
    print(pi_string)
    print(len(pi_string))
        