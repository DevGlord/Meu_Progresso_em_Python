class Carros:
    def __init__(self,modelo,marca='Sei lá'):
        self.modelo = modelo
        self.marca = marca
    def acelerar (self):
        print(f'{self.marca}, {self.modelo}')
        
car = Carros('H10')
car.acelerar()
