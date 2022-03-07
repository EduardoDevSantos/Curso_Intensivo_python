#! /usr/bin/env python3
print("Bem vindo ao RPG Medieval, faça suas escolhas e essas escolhas afetarão seu futuro, então sempre escolha com sabedoria caro jogador, construa sua jornada do heroi aqui e agora!")
player_name = input("Primeiramente, me diga seu nome caro jogador: \n")
print(f"Olá {player_name} seja muito bem vindo, nesse mundo, todos possuem uma classe da qual escolhem para dominar, cada classe possuí habilidades únicas, e cabe a você aprimorar essas habilidades.")
player_class = int(input("Existem duas classes: [1]Guerreiro [2]Mago, faça sua escolha: \n"))
if player_class == 1:
    print(f"Muito bem {player_name} você escolheu a classe Guerreiro, agora tudo depende de você, aprimore-se e faça as escolhas corretas.")
elif player_class == 2:
    print(f"Muito bem {player_name} você escolheu a classe Mago, agora tudo depende de você, aprimore-se e faça as escolhas corretas.")