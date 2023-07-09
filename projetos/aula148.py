import json

class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        print(f'{self.nome} está filmando...')
        self.filmando = True

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c2.filmar()

c1.__dict__['nome'] = ('Sony')


#print(c1.__dict__)
#print(vars(c1))