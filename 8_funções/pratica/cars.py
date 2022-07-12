def info_car(name,model,**informations):
    cars = {}
    cars['name'] = name
    cars['model'] = model
    for key,value in informations.items():
        cars[key] = value
    return cars

car = info_car('MBW Series 3','GP',cost='298.950',color='white',tow_package=True)
print(car)    