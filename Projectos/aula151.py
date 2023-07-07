
class Circulo:
    raio = int(input('raio:'))
    
    @classmethod
    def calcular_area(cls):
        A = 3.14159 * cls.raio ** 2
        return A
    
    @classmethod
    def calcular_circunferencia(cls):
        C = 2 * 3.14159 * cls.raio
        return C
    
print(Circulo.calcular_area())
print(Circulo.calcular_circunferencia())

