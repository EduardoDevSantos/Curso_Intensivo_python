#! /usr/bin/env python3
from audioop import reverse


places = ['canada','united states','santa catarina','rio grande do sul','french']
print("Esses são todos os lugares que eu gostaria de visitar: ",places)
print("Esses são todos os lugares que eu gostaria de visitar porém em ordem alfabética: ",sorted(places))
print("A minha listas em ordem original é essa: ",places)
print("A mesma lista porém em ordem alfabética inversa: ",sorted(places,reverse=True))
print("A lista ainda continua em ordem original: ",places)
places.reverse()
print("A lista agora está invertida: ",places)
places.reverse()
print("Agora minha lista voltou a ordem original: ",places)
places.sort()
print("Agora minha lista está permanentemente em ordem alfabética: ",places)
places.sort(reverse=True)
print("Agora minha lista está permanentemente em ordem alfabética inversa.",places) 