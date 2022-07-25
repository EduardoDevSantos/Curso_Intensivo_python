from random import randint
class Die():
    def __init__(self,sides=20):
        self.sides = sides
    def roll_die(self):
        x = randint(1,self.sides)
        print(x)
my_dado = Die()
my_dado.roll_die()