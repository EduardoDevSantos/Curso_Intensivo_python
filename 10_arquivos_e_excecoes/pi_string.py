# filename = '10_arquivos_e_excecoes/pi_digits.txt'
filename = '10_arquivos_e_excecoes/pi_million_digits.txt'
with open(filename) as file_object: 
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    birthday = input("Enter your birthday, in the form mm/dd/yy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")
    print(pi_string[:52] + "...")
    print(len(pi_string))