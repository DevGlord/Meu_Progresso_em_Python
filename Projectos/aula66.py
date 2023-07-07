""" 
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""
"""
def soma(x,y,z=None, k=12,j = None):
    
    if z is not None:
        print(f'{x=} + {y=} + {z=} + {k} + {j} = ', x + y + z + k + j)  
    else:
        print(f'{x=} + {y=}',x + y) 
    
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(z= 0 , x =7, y= 9,k=12)
"""

