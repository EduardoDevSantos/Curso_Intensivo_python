#! /usr/bin/env python3
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:   # poderia ser usado também uma instrução ELSE. 
    price = 5

print("Your admission cost is $" + str(price) + ".")