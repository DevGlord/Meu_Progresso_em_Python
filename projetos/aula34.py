"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Digite o seu nome:')
tamanho_nome = len(primeiro_nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('O seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('O seu nome é normal.')
    elif tamanho_nome > 6:
        print('O seu nome é muito grande.')
else:
    print('Digite mais de uma letra')
