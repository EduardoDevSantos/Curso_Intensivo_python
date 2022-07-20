class Restaurant():
    """Simula a descrição de um restaurante."""
    def __init__(self,restaurant_name, cuisine_type, open_or_closed):
        """Inicia os atributos restaurant_name e cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_or_closed = open_or_closed
        self.number_served = 0
    def describe_restaurant(self):
        """Mostra o nome do restaurante e o tipo de cozinha."""
        print("\n-->" + self.restaurant_name.title())
        print("-->Tipo de culinária: " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        """Verifica se o restaurante está aberto ou fechado."""
        if self.open_or_closed:
            print("-->O restaurante " + self.restaurant_name.title() +
            " está aberto.")
        else:
            print("-->O restaurante " + self.restaurant_name.title() +
            " está fechado.")
    def set_number_served(self,number_served):
        self.number_served = number_served
        print("Já servimos " + str(number_served) + " pessoas hoje.")
    def increment_number_served(self,peoples):
        self.number_served+=peoples
        print("Já servimos " + str(self.number_served) + " pessoas hoje.")
my_restaurant = Restaurant('ostradamus restaurante','brasileira',True)
# print("O nome do restaurante é: " + my_restaurant.restaurant_name.title() + ".")
# print("O tipo de culinária é: " + my_restaurant.cuisine_type.title() + ".")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant = Restaurant('zucco ristorante','italiana',True)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 100
print("Já servimos " + str(restaurant.number_served) 
+ " pessoas hoje.")
restaurant.set_number_served(250)
restaurant.increment_number_served(30)
