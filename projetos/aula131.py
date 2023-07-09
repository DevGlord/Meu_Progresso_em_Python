
vendas = [
    ('Produto A', 'Segunda', 50),
    ('Produto B', 'Terça', 20),
    ('Produto A', 'Quarta', 30),
    ('Produto C', 'Quinta', 10),
    ('Produto B', 'Sexta', 15),
    ('Produto A', 'Sábado', 20),
    ('Produto C', 'Domingo', 5),
    ('Produto B', 'Segunda', 30),
    ('Produto C', 'Terça', 20),
    ('Produto A', 'Quarta', 15),
    ('Produto B', 'Quinta', 25),
    ('Produto C', 'Sexta', 10),
    ('Produto A', 'Sábado', 35),
    ('Produto B', 'Domingo', 10),
    ('Produto C', 'Segunda', 15),
]

from itertools import groupby

def vend (venda):
    return venda[0]
    
vendas_agrupadas = sorted(vendas,key=vend)
grupos = groupby(vendas_agrupadas,key=vend)

for chave,valor in grupos:
    for grupo in valor:
        total = sum(vendas[2] for vendas in valor)
        print(f'{chave}: R$ {total}')
