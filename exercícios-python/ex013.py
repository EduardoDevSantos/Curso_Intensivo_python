#! /usr/bin/env python3
sexo = int(input("Qual é seu Sexo biologico? [1]Homem [2]Mulher: "))
altura = float(input("Digite sua Altura(em Decimal ex1.70): "))
if sexo == 1:
    peso_ideal = int(72.7 * altura - 58)
elif sexo == 2:
    peso_ideal = int(62.1 * altura - 44.7)
print("Seu peso ideal é: ", peso_ideal)
