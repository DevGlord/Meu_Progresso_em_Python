import json
LOCAL_ARQUIVO = 'aula149_a.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def apresentacao(self):
        print(f'O {self.nome} tem {self.idade} anos.')

cas = Pessoa('Maximiano','18')

cas.apresentacao()
bd = [vars(cas)]

def fazendo_dump():
    with open(LOCAL_ARQUIVO,'w',encoding='utf8') as arquivo:
        print('Fazendo dump')
        json.dump(bd,arquivo,ensure_ascii=False,indent=2)

if __name__ == '__main__':
    print('DUMP')
    fazendo_dump()
