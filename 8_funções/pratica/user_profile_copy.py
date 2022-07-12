from distutils.command.build import build


def build_profile(first,last,**user_info):
    """
    -> (**) Cria um dicionário com um número arbitrário de pares key-value.
    -> Constrói um dicionário contendo tudo que sabemos sobre um usuário.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile 
user_profile = build_profile('albert','einstein',location='princeton',
field='physics')
eduardo = build_profile('eduardo','santos',location='indaial',study='codder',favorite_thing='training')
print(user_profile)
print(eduardo)