from itertools import groupby

# Lista de dicionários com informações de pessoas
pessoas = [
    {'nome': 'João', 'idade': 30},
    {'nome': 'Maria', 'idade': 25},
    {'nome': 'Pedro', 'idade': 30},
    {'nome': 'Ana', 'idade': 25},
]

def ordena(pessoa):
    return pessoa['idade']
# Ordena a lista com base na idade
pessoas_ordenadas = sorted(pessoas, key=ordena)

# Agrupa as pessoas por idade
grupos = groupby(pessoas_ordenadas, key=ordena)

# Itera sobre os grupos e exibe as pessoas de cada grupo
for idade, grupo in grupos:
    print(f'Pessoas com {idade} anos:')
    for pessoa in grupo:
        print(pessoa['nome'])
    print()
        
