favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phill':'python',   
}
for name in sorted(favorite_languages.keys()):
    print(name.title()+ ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())