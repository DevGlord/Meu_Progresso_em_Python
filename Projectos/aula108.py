# Tratamento de erros conteudo do Professor Gustavo Guanabara

try:
    a = int(input('Num:'))
    b = int(input('Num:'))
    r = a / b

except KeyboardInterrupt:
    print('Você digitou CTRL + C e acabou fechando o programa')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, Muito obrigado')

