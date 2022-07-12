def make_sandwich(*toppings):
    print("\nAqui estão os itens do seu sanduíche: ")
    for sandwich in toppings:
        print("->" + sandwich)

make_sandwich('tomate','alface')
make_sandwich('queijo')
make_sandwich('frango','presunto','bacon')
