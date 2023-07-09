class Retangulo:
    largura = int(input('Largura do Retângulo:'))
    altura = int(input('Altura do Retângulo:'))
    
    @classmethod
    def calcular_area(cls):
        calculo = cls.largura * cls.altura
        return calculo
    
    @classmethod
    def calcular_perimetro(cls):
        calculo = (cls.largura ** 2) + (cls.altura ** 2)
        return calculo

print(Retangulo.calcular_area())
print(Retangulo.calcular_perimetro())

    