cubos = []
for value in range(1,11):
    cubos.append(value**3)
print(cubos)

# list comprehension
cubos = [value**3 for value in range(1,11)]
print(cubos)