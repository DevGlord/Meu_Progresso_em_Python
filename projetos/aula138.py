

caminho_arquivo = 'C:\\Users\\maxib\\Contacts\\Desktop\\novo arquivo\\'
caminho_arquivo += 'aula138.txt'

"""
arquivo = open(caminho_arquivo,'w')
 
arquivo.close()
"""
"""
with open(caminho_arquivo,'w+') as arquivo:
    print(type(arquivo))
    arquivo.write('Linha 1\n'),
    arquivo.write('Linha 2\n'),
    arquivo.write('Linha 3\n'),
    arquivo.writelines(('Linha 4\n', 'Linha 5\n'))
    arquivo.seek(0,0)
    print(arquivo.read())
"""
       
with open(caminho_arquivo,'w', encoding = 'utf8') as arquivo:
    arquivo.write('Atenção\n')
"""
arquivo = open("caminho_arquivo",'r+')

arquivo.close()
"""
arquivo = open(caminho_arquivo,'w', encoding= 'utf8')


arquivo.close()