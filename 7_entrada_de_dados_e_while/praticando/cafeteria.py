sandwich_orders = ['atum','pastrami','carne','pastrami','frango','pastrami']
finished_sandwiches  = []
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        print("Estamos sem sanduiches de pastrami no momento.")
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
    else:
        finished = sandwich_orders.pop()
        print("Preparei seu sanduiche de " + finished.title() + ".")
        finished_sandwiches.append(finished)
print("\nAqui estão os sanduiches prontos: ")
for sandwich in finished_sandwiches:
    print(">>>sanduiche de " + sandwich.title() + " pronto.")