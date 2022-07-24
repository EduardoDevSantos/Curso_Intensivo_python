class Restaurant():
    """Simula a descrição de um restaurante."""
    def __init__(self,restaurant_name, cuisine_type, open_or_closed):
        """Inicia os atributos restaurant_name e cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_or_closed = open_or_closed
    def describe_restaurant(self):
        """Mostra o nome do restaurante e o tipo de cozinha."""
        print("°Informações do restaurante")
        print("-->Nome: " + self.restaurant_name.title())
        print("-->Tipo de culinária: " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        """Verifica se o restaurante está aberto ou fechado."""
        if self.open_or_closed:
            print("-->O restaurante " + self.restaurant_name.title() +
            " está aberto.")
        else:
            print("-->O restaurante " + self.restaurant_name.title() +
            " está fechado.")
