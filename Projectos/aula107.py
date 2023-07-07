from sys import getsizeof
"""
def generator():
    var = 'Olá, Mundo!'
    yield 1
    var = 'Bom dia'
    yield var
    var = 'Panela'
    return 'FIM'

g = generator()
print(g)
for v in g:
    print(v)

"""
"""
lista = 'Maximiano'
#print(hasattr(lista, '__iter__'))
if hasattr(lista, 'upper'):
    print('É isso mano')
    print(getattr(lista, 'upper')())
    print(dir(lista))
    print(getsizeof(lista))
else:
    print('Esquece mano')
"""
lista = 'Manuel', 'Victor'

l1 = (x for x in lista)
if hasattr(l1, '__iter__'):
    print('Vem nessa')
    print(getattr(l1, '__next__')())
    print(getattr(l1, '__next__')())
    
    print(getattr(l1, '__next__'))
    #for v in l1:
        #print(v)

else:
    print(l1.close())
    print(l1)
    print('Esquece bro')