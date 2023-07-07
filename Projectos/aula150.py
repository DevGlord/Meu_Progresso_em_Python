class Pessoa:
    ano = 2023
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anônimo',idade)
    
p1 = Pessoa.criar_com_50_anos('Maxi')
print(p1.nome,p1.idade)
p2 = Pessoa.criar_sem_nome(9)
print(p2.nome,p2.idade)

