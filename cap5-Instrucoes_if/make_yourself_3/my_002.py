#! /usr/bin/env python3
current_users = ['admin','gabrielas','edusnts','kauand','joelf','felipez']
new_users = ['luisn','admin','gabrielas','tainap','pauloc']
for user in new_users:
    if user in current_users:
        print("O nome " + user + " Ja foi utilizado.")
    else:
        print("O nome " + user + " Está disponivel.")