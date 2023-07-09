# Exercício - Unir listas
# Crie uma função de zíper (como o zíper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da lista menor.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import itertools

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
l3 = zip(l1,l2)
l4 = itertools.zip_longest(l1,l2,fillvalue= 'Sem Valor')
print(list(l3))
print()
print(list(l4))

def lista(x,y):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2 [i]) for i in range(intervalo) if len(l1) != len(l2) ]#else 'ERRO'

print()
print(lista(l1,l2))