"""
Comandos necessarios:    
    .append
    .pop
    
    """
lista = []
import os 


while True:
        opcao = input(''' Selecione uma opção 
    [i]nserir [a]pagar [l]istar: ''').lower().strip()
        if opcao == 'i':
            os.system('cls')
            adicionar = input('Valor: ')
            lista.append(adicionar)
             
        elif opcao == 'a':
            opcao_a = input(f'Escolha o índice para apagar:')
           
            try:   
                indice = int(opcao_a)
                del lista [indice]
            
            except ValueError:
                print('Por favor digite números inteiros.')
            except IndexError:
                print('Índice não existe na lista.')
            except Exception:
                print('Não sei que erro é esse.')
            
        elif opcao == 'l':
            os.system('cls') 
            
            
            
            if len(lista) == 0:
                print('Nada para listar')
            
            for i, valor in enumerate(lista):
              print(i,valor)  
        else:
            print('Por favor, escolha i, a ou l.') 
            

        


