nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')
if nome and idade:
    print(f'O seu nome é {nome}')
    print(f'A sua idade é {idade}')
    
    print(f'O nome invertido ficará da seguinte forma, {nome[::-1]} ')
    if ' ' in nome:
        print(f'Seu nome contêm espaços.')
    else:
        print(f'Seu nome não contêm espaços.')
    
    print(f'O seu nome contêm {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]} ')
    print(f'A última letra do seu nome é {nome[-1]} ')
else:
   print('Desculpe, você deixou os campos vazios.')

