#! /usr/bin/env python3
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 16

if age_0 >= 18 and age_1 >= 18:
    print("Vocês são maiores de idade")
else: 
    print("Algum de vocês não são maiores de idade.")

if age_0 >= 18 or age_1 >= 18:
    print("Um de vocês é maior de Idade, podem passar!")
else: 
    print("Algum de vocês não são maiores de idade.")