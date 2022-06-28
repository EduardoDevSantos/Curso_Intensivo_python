rivers = {
    'nilo':'egito',
    'amazonas':'brasil',
    'volga':'russia',
}
for river,name in rivers.items():
    print("O " + river.title() + " banha o(a) " + name.title() + ".")
print("\n")
for river in rivers.keys():
    print(river.title())
print("\n")
for name in rivers.values():
    print(name.title())