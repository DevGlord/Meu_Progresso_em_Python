

def msg(var):
    return var


v = msg('Maximiano')

#print(v)


def mult(x,y):
    multp = x * y
    return multp

#n1 = int(input('Numero:'))
#n2 = int(input('Numero:'))

#c = mult(n1, n2)
#print(c)

#print(mult(),type(mult))

def f (var):
    print(var)
    
def dumb():
    return f

#var = dumb()('Exemplo')
var = dumb()

print(id(var),id(f))
    
if var == f:
    print('Manomax')
else:
    print('Joca')

