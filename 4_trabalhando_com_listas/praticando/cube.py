numbers = []
for value in range(1,11):
    numbers.append(value**3)
    print(value**3)

print("Os três primeiros itens da lista são: ")
print(numbers[0:3])

print("\nTrês itens do meio da lista são: ")
print(numbers[3:6])

print("\nOs três últimos itens da lista são: ")
print(numbers[-3:])