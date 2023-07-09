""" try -> Tentar, executar o código

 except -> ocorreu algum erro ao tentar executar
"""

" Forma para converter valor de string para int ou float"
numero_str = input('Digite um valor para ver o dobro:')
try:
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'O dobro do número {numero_float}, é {numero_float * 2}')
except:
    print('Não é um número.')