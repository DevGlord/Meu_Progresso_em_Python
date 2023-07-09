# Manipulando chaves e valores em dicionários 

pessoas = {}

chave = 'nome'

pessoas [chave] = "Maximiano"

sexualidade = 'sexo'
pessoas [sexualidade] = 'M'

print(pessoas)


del pessoas["sexo"]
print(pessoas)
#print(pessoas.clear())
del pessoas["nome"]


if pessoas.get('nome'):
    print(pessoas["nome"])
else:
    print('Não existe')

