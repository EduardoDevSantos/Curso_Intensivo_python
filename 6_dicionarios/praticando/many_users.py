
eduardo = {'first':'eduardo','last':'firmino','location':'iguatu'}
maria = {'first':'maria','last':'gabriela','location':'iguatu',}
jose = {'first':'jose','last':'ferreira','location':'rio de janeiro'}
people = [eduardo,maria,jose]
for name in people:
    full_name = name['first'] + " " + name['last']
    location = name['location']
    print("This is " + full_name.title() + " and your location is " +
        location.title())
