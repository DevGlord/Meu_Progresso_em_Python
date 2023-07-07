import sys
import time
"""
lista = [1,2,3,4,5]

#print(hasattr(lista, '__iter__')) #Iteravel #True

#for v in lista: #Esse for torna-se um iterador
    #print(v)
lista=iter(lista) #agora a lista é iterador
    
#print(hasattr(lista, '__next__')) # False
#lista1 = list(range(100))
#print(sys.getsizeof(lista1))
"""

l1= [x for x in range(100000)] #lista

l2 = (x for x in range(100000)) #generator
#for v in l2:
    #print(v)
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
