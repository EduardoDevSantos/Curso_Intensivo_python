prompt = "Quantos anos o cliente possui"
prompt+= "\nentre com 'quit' para encerrar o programa: "
years = 0
preco = 0
while True:
    years = input(prompt)
    if years != 'quit':
        years = int(years)
        if years >= 12:
            preco = 15
        elif years < 12:
            preco = 10
        elif years <= 3:
            preco = 0
        print("O preço da entrada para este cliente é: $" + str(preco) + ".")
    else: 
        break
    