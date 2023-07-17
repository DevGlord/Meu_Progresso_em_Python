class Pessoa:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        if valor == self._nome:
            self._nome = valor
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,valor):
        self._idade = valor
        
    def imprimir_informacoes(self):
        print(f'O {self._nome} tem {self._idade} anos.')
        return self.imprimir_informacoes

pessoa = Pessoa("João", 25)
print(pessoa.nome)  # Saída: João
print(pessoa.idade)  # Saída: 25
pessoa.imprimir_informacoes()

pessoa.nome = "Maria"
pessoa.idade = 30

print(pessoa.nome)  # Saída: Maria
print(pessoa.idade)  # Saída: 30

pessoa.imprimir_informacoes()