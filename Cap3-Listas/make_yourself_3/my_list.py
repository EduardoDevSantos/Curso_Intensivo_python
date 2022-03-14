#! /usr/bin/env python3
from audioop import reverse
from os import remove


games = ['league of legends','fifa','pokemon fire red'
,'zelda','gta','wild rift']
games[1] = 'pes'
print(games)
games.append('god of war')
print(games)
games.insert(3,'fortnite')
print(games)
del games[3]
print(games)
jogos_concluidos = games.pop(2)
print("Eu zerei: ", jogos_concluidos)
print(games)
remove_game = 'wild rift'
games.remove(remove_game)
print(games)
print("Agora meus jogos estão organizados alfabéticamente",sorted(games))
print("Agora meus jogos estão invertidos alfabéticamente"
,sorted(games,reverse=True))
games.reverse()
print("Agora meus jogos estão invertidos: ",games)
games.reverse()
print("Agora meus jogos voltarão a ordem original: ",games)
games.sort()
print("Agora meus jogos estão permanentemente organizados alfabéticamente: "
,games)
games.sort(reverse=True)
print("Agora meus jogos estão organizados de forma alfabética ,inversa: "
,games)
numero_de_jogos = len(games)
print("Minha lista tem ",numero_de_jogos," jogos")