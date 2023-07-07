# Dictionary Comprehension e Set Comprehension


produto = {
    'nome':'Manteiga',
    'preco': 25.5,
    'Categoria':'Vegetal',
}

novo_dict = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor in produto.items()
}

#print(novo_dict)


lista = [
    ('nome','Manteiga'),
    ('preco', 25.5),
    ('Categoria','Vegetal'),
]

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor in lista
}

#print(dc) 
#print(dict(dc))


setes = {
    
    i for i in lista
}
print(setes)