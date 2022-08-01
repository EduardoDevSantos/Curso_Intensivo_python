local = 'C:/Users/eduar/OneDrive/Documentos/GitHub/Curso_Intensivo_python'
local+= '/10_arquivos_e_excecoes/pi_digits.txt'
with open(local) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())