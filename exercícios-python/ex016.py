#! /usr/bin/env python3
import math
area = float(input("Digite a area em Metros quadrados a ser pintada: "))
num_lata = math.ceil(area / 54)
preco = math.ceil(num_lata * 80)
print("Você precisará de ",num_lata," latas de tintas para pintar tudo.")
print("Isso vai lhe custar R$",preco,",00")