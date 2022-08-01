filename = "10_arquivos_e_excecoes/Prática/guest_book.txt"
while True:
    print("(entre com 'exit' para sair)\n")
    name = input("Qual é seu nome? ").title()
    if name == 'exit'.title():
        break
    print("Olá " + name + " seja bem vindo.")
    with open(filename,'a') as file_object:
        file_object.write(name+" visited \n")