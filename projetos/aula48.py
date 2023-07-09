"""
Lista -> []
Listas em Python
Tipo List - Mutável    
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Metódos úteis: 
append, 
insert, 
pop, 
del, 
clear,
extend, + 

Create Read Update ... Delete
Criar, Ler, alterar,   apagar = lista [i] (CRUD) 
    """
# Entrando no assunto
"""
lista = ['Maximiano',12,'Batista',18]
print(lista)
lista[0] = 'Manuel'
print(lista[-4], type(lista[0]))
print(lista)
"""
# Usando varios comandos das listas
"""
lista = [10, 20, 30, 40]
lista.append(25) # -> Para adicionar um valor a lista 
lista.insert(1,15)  #-> Para adicionar e inserir um valor na lista
lista.pop()  #-> Para remover o ultimo elemento da lista
lista.pop(2)  #-> Para remover um elemento qualquer da lista
lista.remove(10)  #-> Para remover o valor da lista
#lista.clear()  #-> Para limpar a lista, apagar tudo

del lista [3] # -> Para deletar o elemento sugerido
print(lista)

"""
#--------------------------------------

# Usando .append e .insert
"""
lista = [10,20,30,40]
lista.append('Maxi')
nome = lista.pop()
lista.append(333)
lista.insert(3, 'Manuel')
lista.insert(100, 'Maximinao')
lista.insert(7,1323)
print(lista)
print(nome)
"""
#---------------------

# Usando o .extend
"""
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)
"""
# Usando o .copy
"""
lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()  # [:] or .copy
lista_a[0] = 'Não sei'
lista_b [0] = 'Sei de tudo'
print(lista_a)
print(lista_b)
"""
