from guanabara_package import moeda
from time import sleep

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
sleep(0.5)
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
sleep(0.5)
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
sleep(0.5)
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')