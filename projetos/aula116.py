def soma(x,y):
    return x + y

def multiplicar(x,y):
    return x * y

def criar_funcao(funcao,x):
    def algo(y):
        return funcao(x,y)
    return algo

soma_com_cinco = criar_funcao(soma,5)
multiplica_por_dez = criar_funcao(multiplicar, 10)
print(soma_com_cinco(10))
print(multiplica_por_dez(10))
print(soma_com_cinco)
print(multiplica_por_dez)