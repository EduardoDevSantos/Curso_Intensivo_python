favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phill':'python',
}
friends = ['sarah','edward','mike','steven']
for name in favorite_languages:
    print(name.title()+" Obrigado por participar da pesquisa.")
if  friends[2] not in favorite_languages:
    print(friends[2].title()+" Participe da pesquisa por favor.")
if friends[3] not in favorite_languages: 
    print(friends[3].title()+ " Paticipe da pesquisa por favor.")

