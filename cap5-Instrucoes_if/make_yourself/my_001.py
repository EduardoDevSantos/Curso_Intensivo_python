#! /usr/bin/env python3 

# Testando a maior idade: 
age = 17
if age >= 18:
    print("Você é maior de idade")

# Verificando se o PC roda um jogo
placa_de_video = "AMD"

if placa_de_video == "AMD": 
    print("Seu PC roda esse jogo!")

# Estou lendo os livros certos ?
book_1 = 'Revolução dos bixos'
book_2 = '1984 George Orwell'

if book_1 == 'Revolução dos bixos' and book_2 == 'Modernidade liquida': 
    print("Você escolheu os livros certos!")

# Verificando quantas páginas você leu por dia e por semana

pages_day = 5
pages_week = 70

if pages_day == 10 or pages_week == 70:
    print("Você bateu a sua meta de leitura!")

# verificando se o Celular roda um Jogo
memory_ram = 2
if memory_ram >= 3:
    print("Seu celular roda o jogo!")

# Verificando a mochila
bag = ['caneta','caderno','livro']
if 'caneta' in bag and 'caderno' in bag and 'livro' in bag:
    print("Você está pronto para ir para sair.")

pizza_fav = 'Frango com catupiri'
print("Minha pizza favorita é de mussarela ? eu acho que não")
print(pizza_fav == 'Mussarela')

fav_book = 'O nome do vento'
print("Meu livro favorito é o nome do Vento!!")
print(fav_book == 'O nome do vento')

fav_music = 'Mirrors'
print("Minha musica favorita é perfume.")
print('perfume' == fav_music);

fav_anime = 'One piece'
print("One piece é o melhor anime do mundo!!")
print(fav_anime == 'One piece')

fav_movie = 'Gigantes de aço'
print("Gigantes de aço não é meu filme preferido.")
print(fav_movie != 'Gigantes de aço')