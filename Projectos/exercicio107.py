from guanabara_package import moeda
from time import sleep

p = float(input('Digite o preço: R$'))
print(f'A metade de {(p)} é {moeda.metade(p)}')
sleep(0.5)
print(f'O dobro de {(p)} é {moeda.dobro(p)}')
sleep(0.5)
print(f'Aumentando 10%, temos {moeda.aumentar(p)}')
sleep(0.5)
print(f'Reduzindo 13%, temos {moeda.diminuir(p)}')

