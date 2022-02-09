#! /usr/bin/env python3
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Concatenação de Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

#Tabulações e quebras de linha
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\t-Python\n\t-C\n\t-JavaScript")

#Eliminando espaços em branco

favorite_language = 'python '
print(favorite_language+"!")
    # Formas temporárias de se armazenar o valor sem o espaço á direita.
favorite_language.rstrip()
print(favorite_language.rstrip()+"!")
    # Forma permanente
favorite_language = favorite_language.strip()
print(favorite_language)

favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())

favorite_language = ' python '
print(favorite_language+"!")
print(favorite_language.strip()+"!")

