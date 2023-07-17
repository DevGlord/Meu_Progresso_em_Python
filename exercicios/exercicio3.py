class ContaBancaria:
    def __init__(self,saldo,limite):
        self._saldo = saldo
        self._limite = limite
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,valor):
        if valor >= 0:
            self._saldo = valor
        else: 
            print('Valor inválido para o saldo.')
        
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self,valor):
        if valor >= 0:
            self._limite = valor
        else:
            print('Valor inválido para o limite.')
            
    def realizar_saque(self, valor):
            if valor <=  self._saldo + self._limite:
                self._saldo -= valor
                print('Saque realizado com sucesso.')
                return True
            else:
                print('Saldo e limite insuficientes para o saque.')
                return False
        
conta = ContaBancaria(1000,500)
#conta.saldo = 500
#conta.limite = 200

print(conta._saldo)
print(conta._limite)

print(conta.realizar_saque(800))
print(conta.realizar_saque(1000))
print(conta.saldo)

