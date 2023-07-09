primeiro_valor = int(input('Digite um valor:'))
segundo_valor = int(input('Digite outro valor:'))

if primeiro_valor >= segundo_valor:
    print('O primeiro valor é maior que o segundo valor.')
elif primeiro_valor <= segundo_valor:
    print('O segundo valor é maior que o primeiro valor.')
#elif primeiro_valor == segundo_valor:
    #print('Os dois valores são iguais.')
else:
    print('Opção inválida')
print('Programa finalizado.')