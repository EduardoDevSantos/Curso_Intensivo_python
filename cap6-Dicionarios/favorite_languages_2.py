favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phill':'python',
}
friends = ['phill','sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(" Hi "+name.title()+", I see your favorite language is " + favorite_languages[name].title()+"!")

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")
    