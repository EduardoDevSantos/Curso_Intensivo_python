import json
filename = 'favorite_number.json'
def get_number():
    try:
        with open(filename) as f_obj:
            favorite_number  = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
def get_new_user():
    favorite_number = input("What's your favorite number? ")
    favorite_number = int(favorite_number)
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        return favorite_number
def y_number_is():
    favorite_number = get_number()
    if favorite_number:
        print("I know your favorite number, it is " + str(favorite_number))
    else:
        favorite_number = get_new_user()
        print("I'll remember your favorite number.")
y_number_is()
    