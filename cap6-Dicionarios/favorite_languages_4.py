favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phill':['python','haskell']
}
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title()+"'s favorite language is ",end="")
        for language in languages:
            print(language.title())
    else:
        print("\n"+name.title()+"'s favorite languages are: ")
        for language in languages:
            print("\t"+language.title())
