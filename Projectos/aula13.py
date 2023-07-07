nome = 'Maximiano'
altura = 1.60
peso = 46.0
imc = peso / (altura * altura)
"f-strings"
linha_1 = f'{nome} tem {altura :.2f} de altura.'
linha_2 = f'pesa {peso} quilos e o seu imc é {imc :.2f}'

print(linha_1)
print(linha_2)

print(f'{nome}, o seu IMC é {imc :.2f}.')
