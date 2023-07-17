class Circulo:
    def __init__(self,raio):
        self._raio = raio
        
        
    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self,valor):
        if valor > 0:
            self._raio = valor
        
        
    @property
    def area(self):
        return 3.14159 * self._raio**2
        

c1 = Circulo(5)
print(c1.raio)
print(c1.area)