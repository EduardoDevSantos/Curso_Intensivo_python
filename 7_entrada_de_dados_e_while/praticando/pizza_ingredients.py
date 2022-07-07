pizza = []
ingredients = ''
active = 1
prompt = "Quais ingredientes você quer na pizza? digite 1 por vez: "
prompt+= "\n(Digite 'quit' para encerrar.) O máximo de ingredientes é 5."
while active <= 5:
    ingredients = input(prompt)
    if ingredients != 'quit':
        print(">>>O ingrediente " + ingredients + " foi adicionado a pizza.\n")
        pizza.append(ingredients)
        active+=1
        continue
    else:
        break
print("A pizza pedida contém os seguintes ingredientes: ")
for ingredient in pizza:
    print(">>>"+ingredient.title())