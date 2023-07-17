class Retangulo:
    def __init__(self,largura,altura):
        self._largura = largura
        self._altura = altura
        
    @property
    def largura(self):
        self._largura

    @largura.setter
    def largura(self,valor):
        if valor > 0:
            self._altura = valor
    
    @property
    def altura(self):
        self._altura
        
    @altura.setter
    def altura(self,valor):
        if valor > 0:
            self._altura = valor
            
c1 = Retangulo(20,15)
print(c1._altura)
print(c1._largura)