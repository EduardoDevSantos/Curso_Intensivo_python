favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phill':'python',   
}
friends = ['edward','sarah','gabriel','jon']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi " + name.title() + ", Now i know your favorite language!"
        + " your favorite language is " + favorite_languages[name].title() + ".")
    else:
        print("Hi " + name.title()+".")
for name in friends:
    if name not in favorite_languages.keys():
        print("Hi " + name.title() + ", please take our poll!")