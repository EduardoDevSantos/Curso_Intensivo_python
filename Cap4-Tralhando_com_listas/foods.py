#! /usr/bin/env python3
my_foods = ['pizza','falafel','carrot cake']
friend_food = my_foods[:]
my_foods.append('cannoli')
friend_food.append('ice cream')
print("My favorite foods are: ")
for food in my_foods: 
    print(food)

print("\nMy friend's favorite foods are: ")
for food in friend_food:
    print(food)

# Isto não funciona:
# friend_food = my_foods

my_pizzas = ['frango com catupiri','quatro queijos','mussarela']
friend_pizzas = my_pizzas[:]
my_pizzas.append('frango')
friend_pizzas.append('Acabaxi')
print("\nMinhas pizzas favoritas são: ")
for pizza in my_pizzas:
    print(pizza)

print("\nAs pizzas favoritas do seu amigo são: ")
for pizza in friend_pizzas:
    print(pizza)