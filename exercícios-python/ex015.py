#! /usr/bin/env python3
sal_hora = float(input("Digite quanto você recebe por hora trabalhada: "))
hora_trab = int(input("Digite quantas horas você trabalhou no mês: "))
sal_bruto = sal_hora * hora_trab
ir = 11 / 100 * sal_bruto
inss = 8/100 * sal_bruto
sindicato = 5/100 * sal_bruto
descontos = (ir + inss + sindicato)
sal_liquido = sal_bruto - descontos
print("+Salário Bruto: ",sal_bruto,"R$")
print("-IR(11%): ",ir,"R$")
print("-INSS(8%): ",inss,"R$")
print("-Sindicato(5%): ",sindicato,"R$")
print("=Salário Líquido: ",sal_liquido,"R$")