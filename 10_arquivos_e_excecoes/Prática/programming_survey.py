filename = '10_arquivos_e_excecoes/Prática/survey_answers.txt'
while True:
    print("(entre com 'exit' para encerrar)")
    name = input("Qual o nome do usuário? ").lower()
    if name == 'exit':
        break
    answer = input("Por que você gosta de programação? ")
    if answer == 'exit':
        break
    with open(filename, 'a') as file_object:
        file_object.write(name.title() + " = " + answer + "\n")