import os

caminho_arquivo = 'aula139.txt'

with open(caminho_arquivo,'w+', encoding= 'utf8') as arq:
    arq.write('linha 1\n')
    arq.write('ATENÇÃO\n')
    print(arq.read())
    
with open(caminho_arquivo,'a', encoding= 'utf8') as arq:
    arq.write('ATENççççÃÃÃO')
    
os.rename(caminho_arquivo,'aula139-2.txt')