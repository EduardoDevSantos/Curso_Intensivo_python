from collections import OrderedDict
glossary = OrderedDict()
glossary['estrutura_de_repetição'] = 'Repete uma ação um determinado número de vezes.'
glossary['estrutura_condicional'] = 'obdece a testes lógicos para tomar decisões.'
glossary['lista'] = 'são conjunto de dados de mesmo tipo ou diferentes.'
glossary['dicionario'] = 'São conjunto de dados com chave-valor'
glossary['tupla'] = 'são listas imutáveis.'
glossary['variaveis'] = 'armazenam todos os tipos de dados possíveis.'
glossary['inteiros'] = 'são números sem casas decimais.'
glossary['float'] = 'são número que possuem ponto flutuante.'
glossary['string'] = 'é uma cadeia de caracteres envolta por aspas duplas ou simples.'
glossary['bool'] = 'é um valor lógico, retornando apenas Verdadeiro(True) ou Falso(False)'
for key, value in glossary.items():
    print("\n" + key.title())
    print("\t"+value.title())
