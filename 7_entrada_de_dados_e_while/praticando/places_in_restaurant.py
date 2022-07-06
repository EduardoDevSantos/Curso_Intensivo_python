qnt_pessoas = input("Quantas pessoas estão em seu grupo para jantar? ")
qnt_pessoas = int(qnt_pessoas)
if qnt_pessoas > 8:
    print("Vocês deveram esperar uma mesa para " + str(qnt_pessoas) + 
    " pessoas")
else:
    print("A mesa para " + str(qnt_pessoas) + " pessoas está pronta!")