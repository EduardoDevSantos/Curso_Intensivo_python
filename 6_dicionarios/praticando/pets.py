dog = {'tipo':'husky','dono':'eduardo'}
cat = {'tipo':'persa','dono':'aline'}
bird = {'tipo':'bem-te-vi','dono':'jorge'}
pets = [dog,cat,bird]
for pet in pets:
    print("O tipo do animal é " + pet['tipo'].title() + " e seu dono é "
    + pet['dono'].title() + ".") 