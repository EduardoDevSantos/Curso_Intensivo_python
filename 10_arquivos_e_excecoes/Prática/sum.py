while True:
    msg = "Forneça-me dois números e irei somá-los para você."
    print("-----------"+msg+"---------")
    print("(digite 'quit' para sair)")
    a = input("Digite um número: ")
    if a == 'quit': break
    b = input("Digite um segundo número: ")
    if b == 'quit': break
    try:
        a = int(a)
        b = int(b)
        result = a + b
        print("\n"+str(a) + "+" + str(b) + "=" + str(result))
    except:
        print("Você digitou algo errado, tente novamente por favor.")