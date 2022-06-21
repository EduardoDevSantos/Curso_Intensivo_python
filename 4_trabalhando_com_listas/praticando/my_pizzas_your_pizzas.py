pizzas = ['frango','quatro queijos','frango com catupiri','carne de sol']
friend_pizzas = pizzas[:]

pizzas.append('mussarela')
friend_pizzas.append('calabresa')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nAnd my friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)