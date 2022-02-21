#! /usr/bin/env python3

peoples = ['joão','aline','jorge']

print("Olá " + peoples[0].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Como vai " + peoples[1].title() + "? Você foi convidado(a) para um jantar comigo e minha familia.")
print("Tudo bem " + peoples[2].title() + "? Você poderia comparecer a um jantar comigo e minha familia?.")
print(peoples[0].title() + " Não pode comparecer ao jantar.\n")
print("Estou convidando ", len(peoples), " pessoas\n")
peoples[0] = 'Paulo'

print("Olá " + peoples[0].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[1].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[2].title() + " Você foi convidado(a) para um jantar comigo e minha familia.\n")

print("Estou convidando ", len(peoples), " pessoas\n")

print("Encontrei uma mesa de jantar maior!\n")

peoples.insert(0,'ana')
peoples.insert(2,'leandro')
peoples.append('maria')

print("Olá " + peoples[0].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[1].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[2].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[3].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[4].title() + " Você foi convidado(a) para um jantar comigo e minha familia.")
print("Olá " + peoples[5].title() + " Você foi convidado(a) para um jantar comigo e minha familia.\n")
print("Estou convidando ", len(peoples), " pessoas\n")
print("Por conta de uma imprevisto, poderei convidar somente duas pessoas.\n")

srr_people1 = peoples.pop(0).title()
srr_people2 = peoples.pop(0).title()
srr_people3 = peoples.pop(0).title()
srr_people4 = peoples.pop(-1).title()


print("Peço desculpas pelo ocorrido " + srr_people1 + " prometo que em uma próxima vez você será convidado(a).")
print("Peço desculpas pelo ocorrido " + srr_people2 + " prometo que em uma próxima vez você será convidado(a).")
print("Peço desculpas pelo ocorrido " + srr_people3 + " prometo que em uma próxima vez você será convidado(a).")
print("Peço desculpas pelo ocorrido " + srr_people4 + " prometo que em uma próxima vez você será convidado(a).\n")

print("Olá " + peoples[0].title() + " Você ainda é um convidado para o meu jantar, conto com a sua presença.")
print("Olá " + peoples[1].title() + " Você ainda é um convidado para o meu jantar, conto com a sua presença.")
print("Estou convidando ", len(peoples), " pessoas\n")
del peoples[0:2]

print(peoples)
