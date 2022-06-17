# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles.append('Ducati')
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)
from json import tool


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(1,'ducati')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(print("\nA " + too_expensive.title() + " is too expensive for me."))