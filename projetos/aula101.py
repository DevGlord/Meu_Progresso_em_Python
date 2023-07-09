
s1 = {'a12a',12}
#print(dir(s1))
metodo = 'update'
if hasattr(s1, metodo):
    print('Existe sim')
    print(isinstance(s1, str))
    print(getattr(s1, metodo)())

else:
    print('Não existe')

#print(
    #dir(s1))
    
    
