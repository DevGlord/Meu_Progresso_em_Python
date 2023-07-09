class Calculadora:
    
    @classmethod
    def somar(cls,n1,n2):
        soma = n1 + n2
        return soma
    
    @classmethod
    def subtrair(cls,n1,n2):
        subtraindo = n1 - n2
        return subtraindo
    
    @classmethod
    def multiplicar(cls,n1,n2):
        mult = n1 * n2
        return mult
    
    @classmethod
    
    def div(cls,n1,n2):
        if n2 == 0:
            raise ZeroDivisionError('Não dá para dividir Zero por qualquer número.')
        dividir = n1 // n2
        return dividir
    

p1 = Calculadora.somar(10,11)

p2 = Calculadora.subtrair(11,9)
p3 = Calculadora.multiplicar(5,9)
p4 = Calculadora.div(10,2)
print(p1)
print(p2)
print(p3)
print(p4)    