#! /usr/bin/env python3
users = ['admin', 'gabriela', 'kauan02', 'eduz', 'joelf', 'cabainha']
if users:
    for user in users:
        if user == 'admin':
            print("Olá " + user.title() + " Gostaria de ver os relatórios?")
        else:
            print("Olá " + user.title() + " Seja bem vindo de volta!")
else:
    print("Precisamos encontrar alguns usuários!!!")
