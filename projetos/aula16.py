# if.../...elif.../...else 
# if -> Se
# elif -> Se não se
# else -> Se não
entrada = input('Você quer "entrar" ou "sair"?')
if entrada == "entrar":
    print('Você entrou no sistema.')
elif entrada == "sair":
    print('Você saiu do sistema.')
else:
    print('Opção inválida.')
print('Programa finalizado.')