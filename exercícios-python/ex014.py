#! /usr/bin/env python3
peso = float(input("Digite quantos KG de peixe você pescou: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("O seu Excesso de foi de: ",excesso,"KG")
    print("A multa é equivalente á: ",multa,"R$")
else:
    print("Você não irá receber nenhuma multa.")