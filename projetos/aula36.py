"""
Repetições
While (Enquanto)   
Executa uma ação enquanto uma condição for verdadeira    
Loop infinito -> Quando um código não tem fim
Enquanto o while for verdadeiro, ele entra no while, no caso da condicao do exemplo abaixo
mas quando a condicao comecar a ser falso ele não entra mais.

"""
# ----------------------------------------------------------
"""condicao = True
while condicao:
    nome = input('Digite o seu nome:')
    print(f'O seu nome é {nome}')
    
    if nome == 'sair':
        break
print('Acabou')"""
#---------------------------------------------------------------------
"""
#Neste caso vai exibir apenas o 'A' e não o 'OI' porque a condicao é falsa
while False:
    print('OI')
print('A')"""
#--------------------------------------------------------------------
# Enquanto contador for menor que 10
# O valor é falso
# Forma sem o While True
contador = 0
while contador <=  10:
    print(contador)
    contador += 1
print('Acabou')
    
 
#-------------------------------------------------------------------   
    
# Enquanto o valor for menor que 10
# Usando o while True
# O valor é verdadeiro
# Se contador for igual a 10
# Usamos o break para encerrar o programa
# quer dizer, que quando o contador chegar a 10 o programa para
"""while True:
    print(contador)
    contador += 1
    if contador == 10:
        break
print('Acabou')"""