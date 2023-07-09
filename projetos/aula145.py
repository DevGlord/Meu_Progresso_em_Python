
class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Maxi','Batista') #Nova instancia ou objecto
#p1.nome = 'Maxi'
#p1.sobrenome = 'Batista'

p2 = Pessoa('Manuel','Mateus')
#p2.nome = 'Manuel'
#p2.sobrenome = 'Matues'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)
