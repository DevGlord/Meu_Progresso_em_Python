

def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total


      
multiplicacao = mult(4,1,2,5,7)
print(f'O resultado é {multiplicacao}.')

def escolha(numero):    
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'
           
    return opcao
print(escolha(1457))
print(escolha(1270)) 