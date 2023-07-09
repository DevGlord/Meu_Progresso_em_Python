# Operadores Logicos
# and (e), or (ou), not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Quando usamos estes tipos de operadores, temos que ter em conta que precisam ser verdadeiros
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que vc já viu)
# 0 0.0 '' False
# Tbm existe o tipo None que é
# usado para representar um não valor

login = input(' [E]ntrar ou [S]air: ')
senha_digitada = input('Senha:')
senha_aceite = '123456maxi'
if login == 'E' and senha_digitada == senha_aceite:
    print('Login aceite!')
else:
    print('Login Negado!')
print('Programa Finalizado!')
