# 135. Empacotamento


pessoas = {
    'nome':'Aline',
    'sobrenome':'Souza'
    
}

dados_pessoas = {
    'idade' : 16,
    'altura' : 1.6
}

pessoa_completa = {**pessoas,**dados_pessoas}


def testando(*args, **kwargs):
    print('Argumentos Não nomeados:', args)
    
    for chave,valor in kwargs.items():
        print(chave,valor)
    print('Argumentos Nomeados')

#m = int(input('Num:'))
#c = str(input('Marcador:'))

testando( 19,18, nome= 'Maximiano Batista',idade= 18,)
testando(**pessoa_completa)
"""
exemplo = {
    'args1' : 'Manuel',
    'args2' : 2,
    'args3' : 'max',
    'args4' : 'ze',
    
}

testando(**exemplo)

"""


