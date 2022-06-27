users = ['gabriel','maria','edusan','admin','midoriyaSan']
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user.title() + " Do you'll like to see a report?")
        else:
            print("Hello " + user.title() + " Welcome again!")
else:
    print("Precisamos encontrar alguns usuários!")