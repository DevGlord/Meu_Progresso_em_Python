from guanabara_package import moeda
from time import sleep

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
sleep(0.5)
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
sleep(0.5)
print(f'Aumentando 10%, temos {moeda.aumentar(p,88,True)}')
sleep(0.5)
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13,True)}')
