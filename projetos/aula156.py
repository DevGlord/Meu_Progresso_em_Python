
class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self._cor_tampa = None
        
    #def get_cor(self):
        #return self.cor_tinta  

    @property
    def cor(self):
        return self._cor    

    @cor.setter
    def cor (self,valor):
        print('123')
        if valor == 'Vermelho':
            raise ValueError('Não aceito esta cor')
        self._cor = valor
        
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self,valor):
        self._cor_tampa = valor


c1 = Caneta('Azul')
c1.cor = 'blue'
c1.cor_tampa = 'preto'
print(c1.cor_tampa)
#print(c1.get_cor())



