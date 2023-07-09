

a = lambda x,y: x * y 
#print(a(2,6))

lista = [
    ['P1',13],    
    ['P2',6],    
    ['P3',7],    
    ['P4',50],    
    ['P5',8],    
    
]

lista.sort(key=lambda item:item[1],reverse=True)
print(lista)
print(sorted(lista,key=lambda i:i[1],reverse=True))


