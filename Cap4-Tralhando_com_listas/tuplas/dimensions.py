#! /usr/bin/env python3 
dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])

# Erro de tipo:
# dimensions[0] = 350
# Uma tupla é imutável, não se pode mudar seus índices 
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nmodified dimensions: ")
for dimension in dimensions:
    print(dimension)