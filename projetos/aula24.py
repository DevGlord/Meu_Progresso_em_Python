#         in           e     not in
# entre (estar entre) / (não estar entre)  
# Strings são iteráveis
livro = input('Digite um livro:')
escolha = input('Escolha algo dentro do nome do livro:')
if escolha in livro:
    print(f' {escolha} está em {livro}.')
else:
    print(f' {escolha} não está em {livro} ')