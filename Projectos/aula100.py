

#print(dir(s1))

s1 = 'Maximiano'
metodo = 'upper'

if hasattr(s1, metodo):
    print('Existe Upper')
    print(getattr(s1, metodo)())
    

else:
    print('Não existe o metodo',metodo)
    

