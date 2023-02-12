# AJUSTE SALARIAL
def salario(aquisicao):
    usuario = input('Você quer um [D]esconto ou um [A]umento?:').upper()
    if usuario == 'A':
        adicao = aquisicao + (aquisicao * 10 / 100)
        print(f'O salário teve um aumento de {aquisicao:.2f}R$ para {adicao:.2f}R$.')
    elif usuario == 'D':
        subtracao = aquisicao - (aquisicao * 10 / 100) 
        print(f'O salário sofreu um desconto de {aquisicao:.2f}R$ para {subtracao:.2f}R$.')
    else:
        print('Opção inválida.') 
print('\033[1;3;36m         AJUSTE SALARIAL      \033[m')
salario(int(input('\033[1;32m Digite o seu salário: \033[m')))
SS