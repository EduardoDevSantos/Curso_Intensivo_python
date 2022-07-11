def city_country(cname,country):
    f_message = cname + "," + country
    return f_message.title()
message = city_country('santa catarina','brasil')
print(message)
message = city_country('tokyo','japão')
print(message)
message = city_country('são paulo','brasil')
print(message)