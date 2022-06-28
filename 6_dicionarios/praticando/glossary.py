glossary = {
    'estrutura_de_repetição':'Repete uma ação um determinado número de vezes.',
    'estrutura_condicional':'obdece a testes lógicos para tomar decisões.',
    'lista':'são conjunto de dados de mesmo tipo ou diferentes.',
    'dicionario':'São conjunto de dados com chave-valor',
    'tupla':'são listas imutáveis.',
    'variaveis':'armazenam todos os tipos de dados possíveis.',
    'inteiros':'são números sem casas decimais.',
    'float':'são número que possuem ponto flutuante.',
    'string':'é uma cadeia de caracteres envolta por aspas duplas ou simples.',
    'bool':
    'é um valor lógico, retornando apenas Verdadeiro(True) ou Falso(False)',
}
for key,value in glossary.items():
    print("\n" + key.title())
    print("\t"+value.title())