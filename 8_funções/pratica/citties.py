from pydoc import describe


def describe_city(cidade,pais='brasil'):
    print("A cidade de " + cidade.title() 
    + " está localizada no(a) " + pais.title() + ".")
describe_city('santa catarina')
describe_city('são paulo')
describe_city('tokyo')