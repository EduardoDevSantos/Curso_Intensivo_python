cities = {
    'santa catarina':{'country':'brasil','population':7.165,
    'fact':'É conhecida por suas praias e montanhas.'},
    'new york':{'country':'estados unidos','population':8.38,
    'fact':'Possui o enorme Central Park e o Empire State Building.'},
    'toquio':{'country':'japão','population':13.96,
    'fact':'É uma cidade muito movimentada e ultramoderna.'}
}
for k,v in cities.items():
    print("\nA cidade de " + k.title() + " está cituada no país " + 
    v['country'].title() + " tem população de " + str(v['population']) + 
    ' milhões de pessoas, e um fato sobre a cidade é que ' + v['fact'])    