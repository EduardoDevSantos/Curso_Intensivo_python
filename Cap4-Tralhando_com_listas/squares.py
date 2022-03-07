#! /usr/bin/env python3
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Usando list comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)