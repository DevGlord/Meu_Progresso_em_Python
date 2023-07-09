"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

l3 = []
for i in range(len(lista_b)):
    l3.append(lista_a[i] + lista_b[i])
print(l3)    

"""
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
l3 = []
for i,_ in enumerate(lista_b):
    l3.append(lista_a[i] + lista_b[i])
print(l3)
"""

lista_a = [10, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
l3 = [x + y for x,y in zip(lista_a,lista_b)]
print(l3)