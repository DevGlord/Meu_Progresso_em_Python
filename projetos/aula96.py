# Dicionario comprehension
produto = {
    'nome':'Manteiga',
    'preco': 25.5,
    'Categoria':'Vegetal',
}
dc = {
    chave:valor
    for chave,valor in produto.items()
}
print(dc)
print()
#-----------------------
# set comprehension
produtos1 = {
    'nome','Manteiga',
    'preco', 25.5,
    'Categoria','Vegetal',
}

s1 = {i10 for i10 in produtos1}
print(s1)
print()
#------------
# set e dicionario em comprehension
produto2 = {
    ('nome','Manteiga'),
    ('preco', 25.5),
    ('Categoria','Vegetal'),
}

df = {
    i for i in produto2
}
print(df)
dv = {
    chave: valor
    for chave, valor in produto2
}
print()
print(dv)
print()
