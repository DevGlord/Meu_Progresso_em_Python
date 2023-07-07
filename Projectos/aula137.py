# Funções Recursivas e recursividade 

"""
def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(11))

from math import factorial

v = factorial(5)
print(v)
"""
def soma_recursiva(n):
    if n <= 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)
    
print(soma_recursiva(10))