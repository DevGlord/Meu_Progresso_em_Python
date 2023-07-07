"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)  
    """
    
def soma(z,x,y):
    #Definição
    print(f'{x = } + {y = } + {z = } =', x + y + z)
    
soma(y= 12, z= 100, x= 13)
print(12,100,13, sep='-')