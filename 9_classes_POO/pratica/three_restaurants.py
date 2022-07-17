from this import d


class Restaurant():
    """Simula a descrição de um restaurante."""
    def __init__(self,restaurant_name, cuisine_type, open_or_closed):
        """Inicia os atributos restaurant_name e cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_or_closed = open_or_closed
    def describe_restaurant(self):
        """Mostra o nome do restaurante e o tipo de cozinha."""
        print("\n-->" + self.restaurant_name.title())
        print("-->Tipo de culinária: " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        """Verifica se o restaurante está aberto ou fechado."""
        if self.open_or_closed:
            print("\n-->O restaurante " + self.restaurant_name.title() +
            " está aberto.")
        else:
            print("\n-->O restaurante " + self.restaurant_name.title() +
            " está fechado.")
my_restaurant = Restaurant('zucco ristorante','brasileira',False)
your_restaurant = Restaurant('ristorantino','chinesa',True)
the_restaurant = Restaurant('Restaurante La Farina','italiana',False)

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
the_restaurant.describe_restaurant()

my_restaurant.open_restaurant()
your_restaurant.open_restaurant()
the_restaurant.open_restaurant()