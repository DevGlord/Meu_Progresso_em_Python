"""
Imprecisão de ponto flutuante




"""
import decimal 



n1 = decimal.Decimal (0.1)
n2 = decimal.Decimal (0.7)
n3 = n1 + n2
print(round(n3,2))
print(f' {n3:.2f} ')
print(n3)