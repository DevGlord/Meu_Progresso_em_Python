# Shallow copy vs Deep Copy em dados mutáveis Python

# Shallow copy

"""
dados = {
    "nome":"Maximiano",
    "sobrenome":"Batista",
    "idade":[18,19,20],
}

dados2 = dados.copy()
dados ["idade"][1] = 9999999 
print(dados)
print(dados2)

"""
import copy

dados = {
    "nome" : "Maximiano",
    "idade" : [18,19,20],
    
}
dados2 = copy.deepcopy(dados)
dados["idade"][1] = 9999999999 # or dados ["idade"].append(9999999) porque o [18,19,20] esses numeros estao dentro de uma lista

print(dados)
print(dados2)
