current_users = ['julysa31','edusan421','couldesx12','gabivieira312','yuire_31']
new_users = ['kauan_d94','bras_penta','edusan421','Gabivieira312','john_nev3r']
for user in new_users:
    if user.lower() in current_users:
        print("O nome de usuário " + user + " está em uso.")
    else:
        print("O nome de usuário " + user + "está disponível.")