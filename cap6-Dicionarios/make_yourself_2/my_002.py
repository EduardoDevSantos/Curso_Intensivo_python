rios = {
    'amazonas':'america do sul',
    'mississippi':'estados unidos',
    'volga':'europa',
}
for k,v in rios.items():
    print("O "+k.title()+" faz parte do(a) "+v.title())
for rio in rios:
    print(rio.title())
for lugar in rios.values():
    print(lugar.title())