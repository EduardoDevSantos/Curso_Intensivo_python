#! /usr/bin/env python3
current_users = ['admin'.upper(),'gabrielas'.upper(),'edusnts'.upper(),'kauand'.upper(),'joelf'.upper(),'felipez'.upper()]
new_users = ['luisn'.upper(),'ADMIN'.upper(),'gabrielas'.upper(),'tainap'.upper(),'pauloc'.upper()]
for user in new_users:
    if user in current_users:
        print("O nome " + user.title() + " Ja foi utilizado.")
    else:
        print("O nome " + user.title() + " Está disponivel.")