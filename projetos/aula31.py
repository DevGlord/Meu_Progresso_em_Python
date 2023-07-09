"""v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))"""

"""
Flag (Bandeira) - Marcar um locaç
None - Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""
condicao = True
passou_no_if = None
print('Deixa exprimentar algo aqui...')
if condicao:
    passou_no_if = True
    print('Não passou no if')
else:
    print('Passou no if')
if passou_no_if:
    print(passou_no_if,passou_no_if is None)
else:
    print(passou_no_if,passou_no_if is not None)