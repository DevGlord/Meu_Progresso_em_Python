# Métodos úteis nos dicionários Python (dict) (parte 2)

p1 = {
    "nome":"Max",
    "idade":18,
    
}

#print(p1.get("nome"))
#p1.pop("nome")
#print(p1)

#p1.popitem() # apaga a ultima chave do dict

#p1.update({
#    "nome" : "Manuel",
#    "sobrenome" : "Maximiano",
    
#})
#p1.update(nome="Manuel", sobrenome="Alberto")

tupla = (('nome','Maximiliano'), ('idade',30))
#p1.update(tupla)
lista = [['nome','Maximiliano'], ['idade',30]]
p1.update(lista)
print(p1)

