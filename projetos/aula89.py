# list comprehension
#print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
    
lista = [numero * 2
         for numero in range(10)]
#print(lista)


produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 ) > 10
]


print(*novos_produtos, sep='\n')



