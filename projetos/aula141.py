
from guanabara_package import aula142
try: 
    print('''
                   MENU
    [1] Escolher a moeda para a conversão
    [2] Ver todas as opções de moedas
    [3] Fechar o programa
    ''')

    opcao = int(input('Escolha uma opção:'))
    
    
    if opcao == 1:
        moeda = str(input('Qual a moeda que você quer?'))
        print(aula142.config(moeda))
        
    elif opcao == 2:
        print(aula142.diferentes_moedas())
     
     
        
finally:
    ...
    
    