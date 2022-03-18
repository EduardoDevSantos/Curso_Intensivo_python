#! /usr/bin/env python3
car = 'BMW'
print("Meu carro é uma Lamborguini ?")
print(car == 'Lamborguini')

meus_livros = ['O nome do vento','Duna','Sherlock']
print("O primeiro livro da minha estante é O nome do vento!!")
print('O nome do vento' == meus_livros[0])

ban_users = ['eDUardO','NucaDox','GorD0x']
print('eduardo' == ban_users[0].lower())
print('gordox' == ban_users[2].lower())

nota_1 = 10
nota_2 = 8
nota_3 = 9
nota_4 = 5
soma_das_medias = nota_1 + nota_2 + nota_3 + nota_4 
print("A minha nota do primeiro bimestre é um 10!!!")
print(nota_1 == 10)
print("No segundo bimestre eu fiquei acima da média!!")
print(nota_2 > 6)
print("A minha nota no terceiro bimestre foi abaixo da média ;-;")
print(nota_3 < 6)
print("No último bimestre eu me esforçei muito e fiquei acima na media")
print(nota_4 >= 6)
print("A minha média não foi o suficiente para passar de ano")
print(soma_das_medias <= 24)

print("Minhas duas primeiras notas foram acima da média")
print(nota_1 > 6 and nota_2 > 6)
print("Minhas duas últimas notas foram acima de 9")
print(nota_3 > 9 or nota_4 > 9)

itens = ['espada','escudo','poção','livro de feitiços','keys']
if 'keys' in itens:
    print("Você pode passar para a pŕoxima fase, você possui as chaves.")
print("Você têm a lança para enfrentar o chefe final?")
print('lança' in itens)

