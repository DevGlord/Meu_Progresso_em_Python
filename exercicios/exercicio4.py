class Produto:
    def __init__(self,nome,preco,desconto):
        self._nome = nome
        self._preco = preco
        self._desconto = desconto
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome = valor
        
    @property
    def preco(self):
        return self._preco
        
    @preco.setter
    def preco(self,valor):
        self._preco = valor
    
    @property
    def desconto(self):
        return self._desconto
        
    @desconto.setter
    def desconto(self,valor):
        if valor > 0:
            self._desconto = valor
        else:
            print("Valor inválido para o desconto.")
            
    def preco_com_desconto(self):
        return self._preco * (1 - self.desconto / 100)
            
produto = Produto("Camiseta", 50, 10)
"""
print(produto.nome)  # Saída: Camiseta
print(produto.preco)  # Saída: 50
print(produto.desconto)
"""
produto.nome = "Calça"
produto.preco = 80
produto.desconto = 20

print(produto.nome)  # Saída: Calça
print(produto.preco)  # Saída: 80
print(produto.desconto)  # Saída: 20
print(produto.preco_com_desconto())