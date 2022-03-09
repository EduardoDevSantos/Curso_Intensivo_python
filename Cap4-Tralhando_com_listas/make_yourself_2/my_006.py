#! /usr/bin/env python3
cubos = []
for value in range(1,11):
    cubos.append(value**3)
print(cubos)

# list comprehension
cubos = [value**3 for value in range(1,11)]
print(cubos)

print("Os três primeiros itens da lista são: ")
print(cubos[:4])

print("Os três itens do meio são: ")
print(cubos[4:7])

print("Os três últimos itens da lista são: ")
print(cubos[-3:])