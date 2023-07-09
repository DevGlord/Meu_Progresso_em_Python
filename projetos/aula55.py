"""
Split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Eu sou o Maxi, Tudo bem com você?'
lista_frase_crua = frase.split(',')

lista_frase = []
for i, valor in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())
frase_unida =  ', '.join(lista_frase)
print(frase_unida)