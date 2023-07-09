def cliente(nome, lista = None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = cliente('Luiz')
cliente1.append('Mario')
cliente2 = cliente('Manuel')
cliente('Manuel',cliente2)
cliente2.append('Gaspar')

cliente('Manuel',cliente1)

print(cliente1)
print(cliente2)

