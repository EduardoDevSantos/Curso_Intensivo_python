def info_car(name,model,**informations):
    """Cria um dicionário contendo informações de um módelo de carro."""
    cars = {}
    cars['name'] = name
    cars['model'] = model
    for key,value in informations.items():
        cars[key] = value
    return cars
