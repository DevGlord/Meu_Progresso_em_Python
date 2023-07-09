# For 
# range -> range(start,stop,step)
#                 (comeca,termina,pula)   


"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

"""numeros = range(0,-10,-2)
for numero in numeros:
    print(numero)"""
    
"""texto = iter('luiz') #.__iter__()
print(next(texto)) #.__next__
print(next(texto))
print(next(texto))
print(next(texto))"""

"""
# for letra in texto
texto = 'luiz' # iteravel
for letra in texto:
    iterador = iter(texto) #iterador

    print(letra)
"""
texto = 'luiz' # iteravel
iterador = iter(texto) #iterador
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
