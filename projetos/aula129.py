vendas = [    ('Produto A', '10/01/2022', 50),    ('Produto B', '11/01/2022', 20),    ('Produto A', '12/01/2022', 30),    ('Produto C', '13/01/2022', 10),    ('Produto B', '14/01/2022', 15),    ('Produto A', '15/01/2022', 20),    ('Produto C', '16/01/2022', 5),    ('Produto B', '17/01/2022', 30),    ('Produto C', '18/01/2022', 20),    ('Produto A', '19/01/2022', 15),    ('Produto B', '20/01/2022', 25),    ('Produto C', '21/01/2022', 10),    ('Produto A', '22/01/2022', 35),    ('Produto B', '23/01/2022', 10),    ('Produto C', '24/01/2022', 15),]

from itertools import groupby

def loja(vendas):
    return vendas[0]

vendas_agrupadas = groupby(sorted(vendas, key=loja), key=loja)
for produto,grupo in vendas_agrupadas:
    total_vendas = sum(venda[2] for venda in grupo)
    print(f"Produto: {produto} - Total de Vendas: {total_vendas}")
    

