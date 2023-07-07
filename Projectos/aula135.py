from types import GeneratorType


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

 
generatore = (round(x ['preco'] * 1.1,2 ) for x  in produtos)
print(list(generatore))
print(f'é um generator? {isinstance(generatore, GeneratorType )}')
novos_produtos = list(map(lambda x: round(x['preco'] * 1.1,2), produtos))
print(novos_produtos)

