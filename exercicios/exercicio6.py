class Carro:
    def __init__(self,marca,modelo,ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,valor):
        self._marca = valor
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self,valor):
        self._modelo = valor
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self,valor):
        self._ano = valor
    
    def informacoes(self):
        return (f'O {self.marca} tem o modelo {self.modelo} e é do ano {self.ano}')
        
carro = Carro("Toyota", "Corolla", 2020)
print(carro.marca)  # Saída: Toyota
print(carro.modelo)  # Saída: Corolla
print(carro.ano)  # Saída: 2020

carro.marca = "Honda"
carro.modelo = "Civic"
carro.ano = 2022

print(carro.marca)  # Saída: Honda
print(carro.modelo)  # Saída: Civic
print(carro.ano)  # Saída: 2022

print(carro.informacoes())