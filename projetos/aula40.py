nome = input('Digite um nome:')

indice = 0 
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)


# O objectivo é por (*) entre cada letra do nome
#nova_string = '*'
