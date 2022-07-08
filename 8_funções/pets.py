from pydoc import describe


# Abaixo usamos um valor default para animal_type
def describe_pet(pet_name,animal_type='dog'):
    """Exibe informações sobre um animal de estimação, 
    usando argumentos posicionais e nomeados"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')  # Posicional
describe_pet(pet_name='willie',animal_type='dog')  # Nomeado
describe_pet('leona')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet('harry','hamster')
describe_pet(animal_type='hamster',pet_name='harry')