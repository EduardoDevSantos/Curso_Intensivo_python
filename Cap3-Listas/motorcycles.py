#! /usr/bin/env python3
# Substituindo valores
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
#Append
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
# Insert
motorcycles.insert(0,'ducati')

print(motorcycles)
# Del
del motorcycles[0]
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yahama','suzuki']
print(motorcycles)
# POP
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owened was a ' + first_owned.title() + '.')

#remove

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive.title() + " is too expensive for me.")


