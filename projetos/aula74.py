"""
Introdução ao tipo de dados dict - Dicionários em Python

"""

teste = {"nome" :["Maximiano", "André"], "idade" : [18 , 45]} #, {"nome" :["Mbappe", "Jullian"], "idade" : [20 , 15]}
teste ["sobrenome"] = ["Batista", "Salazar"]

print(f'\033[1;3;36m{teste.values()}\033[m') #[0]["nome"])
print(f'\033[1;3;36m{teste.keys()}\033[m') #[1]["idade"])
print(f'\033[1;3;36m{teste.items()}\033[m') #[1]["idade"])
print(teste)
print(f'\033[1;3;32m O sr.{teste["nome"][0]} é irmão do sr.{teste["sobrenome"][0]}\033[m')
for chave in teste:
    print(f'\033[1;3;33m{chave}{teste[chave]}\033[m')
    

# Fazer anotações!
    """Dicionário
    Para adicionar mais valores dentro das chaves (nomes:) tenho que adicionar os valores
    dentro de uma lista, 
    
    teste = {"nome" :["Maximiano", "André"]}
    teste -> variavel que está o dicionário
    {} -> dicionário
    "nome" -> 
    ["Maximiano", "André"] -> lista onde foi adicionada os valores
    """

