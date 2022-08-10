import json
def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_user():
    """Saúda o usuário pelo nome.""" 
    username = get_stored_username()
    confirm_username = input("You're " + username + "? [Y]es [N]o: ").lower()
    if confirm_username == 'n':
        username = get_new_username()
        print("We'll remeber you when you come back, " + username + "!")
    else:
        if username:
            print("Welcome back, " + username.title() + "!")
        else:
            username = get_new_username()
            print("We'll remeber you when you come back, " + username + "!")
greet_user()