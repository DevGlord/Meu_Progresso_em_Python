
numeros = [1,2,3,4,5,6,7,8,9]
novos_numeros = [
    numero 
    if numero != 6 else 600 # neste caso é obrigatorio usar a condicao inteira
    for numero in numeros 
    if numero % 2 == 0
         
]

#print(novos_numeros)



linhas_e_colunas = [
    (x, y) if y != 2 else (x, y * 1000)
    for x in range(3)
    for y in range(3)
]

#print(linhas_e_colunas)

string = 'Maximiano Batista'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string),numero_de_letras)
    ])

#print(nova_string)

nomes = ['maxi','luiz','helena','joana','felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
    
    ]


#print(novos_nomes)

numeros = [[numero, numero ** 2] for numero in range(10)]

flat = [y for x in numeros for y in x]
#print(numeros)
#print(flat)


