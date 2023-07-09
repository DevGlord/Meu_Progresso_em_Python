import random as rd

""" Para gerar mais de um cpf é só fazer isto:
for a in range(100)
e depois dar um tab em tudo
"""
# for _ in range(10): # para gerar 10 cpfs ao mesmo tempo
nove_digitos = ''
for i in range(9):
    nove_digitos += str(rd.randint(0, 9)) 

contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11


resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado_pelo_calculo = f' {nove_digitos}{digito_1}{digito_2}'
print(f'O cpf{cpf_gerado_pelo_calculo} é válido.')


