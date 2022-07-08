prompt = "Se pudesse visitar um lugar no mundo, para onde você iria? "
respostas = {}
active = True
while active:
    nome = input("Qual é o seu nome? ") 
    resposta = input(prompt)
    respostas[nome] = resposta
    denovo = input("Outra pessoa para responder? [s]sim [n]não: ").lower()
    if denovo == 'n':
        active = False

print("---Resultado da pesquisa---")
for n,r in respostas.items():
    print(n.title() + " Gostaria de visitar " + r.title() + ".")