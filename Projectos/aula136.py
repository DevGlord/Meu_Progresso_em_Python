
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

from functools import reduce

total = reduce(lambda x,y : x+y['preco'],produtos,0)
print(total)

"""
novos_produtos = [
    p for p in produtos
    if p['preco'] > 100
]
print(novos_produtos)
"""
"""
novos_produtos = list(filter(lambda x: x['preco'] <= 50,produtos))
print(novos_produtos)
"""


