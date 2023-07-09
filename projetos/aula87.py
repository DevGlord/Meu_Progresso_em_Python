# 134. Funções lambda complexas (para entendimento)
"""
salario = int(input("Salário:"))

imposto = lambda x: x * 0.25

print(f'O imposto é {imposto(salario):.2f}R$')

"""
"""
precos = [100, 500, 10, 25]


impostos = list(map(lambda x: x * 0.3, precos))

print(impostos)

for item in impostos:
    print(f'O valor do imposto é {item :.2f}R$')
    
"""


