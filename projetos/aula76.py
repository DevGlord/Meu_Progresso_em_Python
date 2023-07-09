# Métodos úteis dos dicionários em Python

pessoas = {
    'nome' : 'Maximiano',
    'sobrenome' : 'Batista',
    
    
}

#print(f'O dicionário tem {pessoas.__len__()} chaves.')
#print(pessoas.keys())
#print(pessoas.values())
print(pessoas.items())

#for chave in pessoas.keys():
    #print(chave)
#for valor in pessoas.values():
    #print(valor)
    
pessoas.setdefault('idade',10)

print(pessoas)