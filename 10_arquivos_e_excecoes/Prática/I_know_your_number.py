import json
filename = 'favorite_number.json'
with open(filename) as f_obj:
    favorite_number = json.load(f_obj)
    print("I know your favorite number, it is " + str(favorite_number))