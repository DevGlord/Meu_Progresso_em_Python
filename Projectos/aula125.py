from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from itertools import groupby

def print_iter():
    for pessoa in combinations(pessoas, 2):
     
        print(pessoa)
        print()
        
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca' ],
    ['p', 'm', 'g'],
    ['masculino','femenino','unisex'],
    ['algodão','poliester']

]
print_iter()
print()

print(list(combinations(pessoas, 2)))
print()

print(list(permutations(pessoas)))
print()
print(list(product(*camisetas)))

print('------------------')
print(f'Groupy{list(groupby(camisetas))}')
