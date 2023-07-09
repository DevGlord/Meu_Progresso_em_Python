login = input(' [E]ntrar ou [S]air: ')
senha_digitada = input('Senha:') or 'Sem senha'
senha_aceite = '123456maxi'
if login == 'E' or login == 'e' and senha_digitada == senha_aceite:
    print('Login aceite!')
else:
    print('Login Negado!')
print('Programa Finalizado!')