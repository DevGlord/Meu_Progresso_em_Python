print('\033[1;3;30m Calculadora usando While\033[m')
while True:
#--------------------------------------------------
    n1 = input('Digite um número:')
    n2 = input('Digite outro número:')
    operadores = input('Digite o operador +-/*')
    
    numeros_validos = None
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
       numeros_validos = None
       
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operadores not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operadores) > 1:
        print('Digite apenas um operador.')
#--------------------------------------------------------   
    print('Realizando a sua conta. Confirá o resultado:')
    if operadores == '+':
        print(f'{n1_float} + {n2_float} =', n1_float + n2_float)
    elif operadores == '-':
         print(f'{n1_float} - {n2_float} =', n1_float - n2_float)
    elif operadores == '/':
         print(f'{n1_float} / {n2_float} =', n1_float /n2_float)
    elif operadores == '*':
         print(f'{n1_float} * {n2_float}= ', n1_float * n2_float)
    else:
        print('Não deveria ter chegado aqui.')
#------------------------------------------------------------
    sair = input('\033[1;3;33m Quer sair? [S]im ou [N]ão: \033[m').lower().startswith('s')
    
    if sair is  True:
        break

    