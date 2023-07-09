

l1 = [lista for lista in range(10)] # list comprehension



produto2 = [
    ('nome','Manteiga'),
    ('preco', 25.5),
    ('Categoria','Vegetal'),
]

d1 = {
    chave:valor
    for chave,valor  in produto2
}

#print(d1)

s1 = {chave for chave in produto2}
#print(s1)

nome = 'Maxi1'
print(isinstance(nome, (int)))
      