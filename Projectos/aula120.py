
def fabrica(a=None,b=None,c=None):
    def decorador(funcao):
        print('DECORADOR1')
        
        def aninhada(*args, **kwargs):
            print('Aninhada')
            res = funcao(*args, **kwargs)
            return res
        return aninhada
    return decorador



@fabrica(1,2,3)
def soma(x,y):
    return x + y

mano = soma(10,4)
print(mano)

#decorar = fabrica()
#mult = decorar(lambda x, y: x * y)


#eno = mult(10,4)

#print(meno)
