#! /usr/bin/env python3
from audioop import reverse

# Organizando permanentemente.
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
#Organizando temporáriamente.
cars = ['bmw','audi','toyota','subaru']
print("\nHere is the original list: \n",cars)

print("\nHere is the sorted list: \n",sorted(cars))

print("\nHere is the original list again: \n",cars)

print("\nHere is the inverse sorted list: \n",sorted(cars ,reverse=True),"\n")
# Invertendo a ordem original
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)
#Tamanho de uma lista.

cars = ['bmw','audi','toyota','subaru']
print(len(cars))
