"""class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def apresentar(self):
        print(f'Este é um {self.ano} {self.marca} {self.modelo}')

Car = Carro('Hyundai','I10', '2012')
Car.apresentar()
"""

"""
class Cachorro:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        print(f'O cachorro {self.nome} tem {self.idade} anos.')
        
cao = Cachorro('Douglas', '2')
cao.latir()
"""


"""
class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0
        
    def depositar(self,valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else: 
            print("Saldo insufeciente. Não é possível realizar o saque.")
    
    def mostrar_saldo(self):
        print(f"Saldo atual do banco {self.nome}: {self.saldo}")

banco = Banco("BFA")
banco.mostrar_saldo()

banco.depositar(500)
banco.mostrar_saldo()

banco.sacar(1000)
banco.mostrar_saldo()

"""