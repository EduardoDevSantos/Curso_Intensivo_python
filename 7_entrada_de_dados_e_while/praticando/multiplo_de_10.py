message = "Me fale um numero e direi se ele é ou não um múltiplo de 10: "
number = input(message)
number = int(number)
if number % 10 == 0:
    print("O número " + str(number) + " é um múltiplo de 10.")
else:
    print("O número " + str(number) + " não é um múltiplo de 10.")