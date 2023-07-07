# raise

def divisao (n1,n2):
    if n2 == 0:
        raise ZeroDivisionError('Deu erro, e já entendi isto')
        
    else:
        return n1/n2
try:
    n3 = divisao(10, 0) 
    print(n3)   
except ZeroDivisionError as error:
    print(error)

