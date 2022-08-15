def city_country(city,country,population=0):
    if population:
        output = city.title() + ", " + country.title() + " - população " 
        output+= str(population)
    else:
        output = city.title() + ", " + country.title()
    return output
