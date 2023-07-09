
class Banco:
    def __init__(self,nome):
        self.nome = nome
        self._informacoes = None
        self._idade = None
        self._saldo = None
        self._sacar = None
        self._total_restante = None
        self._deseja_continuar = None
        self._opcoes = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,valor):
        if valor < 18:
            raise ValueError('Esta ação não é permitida para menores de 18 anos')
        self._idade = valor

    @property
    def informacoes(self):
        return self._informacoes

    @informacoes.setter
    def informacoes(self,valor):
        print(f'''Nome: {self.nome}
                  Idade: {self.idade}''')
        self._informacoes = valor

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,valor):
        print(f'Você tem {valor}$ na conta.')
        self._saldo = valor

    @property
    def sacar(self):
        return self._sacar

    @sacar.setter
    def sacar(self,valor):
        if valor > self.saldo:
            raise ValueError('Levantamento negado! não tem dinheiro suficiente na conta.')
        else:
            print('Levantamento feito com sucesso.')
        self._sacar = valor

    @property
    def total_restante(self):
        return self._total_restante

    @total_restante.setter
    def total_restante(self,valor):
        total = self.saldo - self.sacar
        print(f'No total sobrou {total}$')
        if self.sacar > self.saldo:
            raise ValueError('Aconteceu um erro no sistema.')
        self._total_restante = valor

    @property
    def deseja_continuar(self):
        return self._deseja_continuar

    @deseja_continuar.setter
    def deseja_continuar(self,valor):
        if valor in 'SsNn':
            if valor == 'Ss':
                ...
            else:
                print('PROGRAMA ENCERRADO')
        else:
            raise ValueError('DIGITO INVÁLIDO')
        self._deseja_continuar = valor

    @property
    def opcoes(self):
        return self._opcoes

    @opcoes.setter
    def opcoes(self,valor):

        self._opcoes = valor



c1 = Banco('Manuel')
c1.deseja_continuar =  input('Deseja continuar? [S] ou [N]:')
c1.idade = 18
c1.saldo = int(input('Quanto dinheiro você tem?'))
c1.sacar = int(input('Quanto dinheiro você deseja levantar?'))
c1.total_restante = True
c1.opcoes = input('Escolhe uma opção:')
#print(c1.nome)
#print(c1.idade)
"""
while True:
    print('''
    O QUE DESEJA VER???
        [1] INFORMAÇÕES
        [2] SALDO DA CONTA
        [3] SACAR 
        [4] TOTAL RESTANTE NA CONTA
        [5] SAIR
    ''')

    if Banco.opcoes == 1:
        Banco.informacoes()
        break
    elif Banco.opcoes == 2:
        Banco.saldo()
        break
    elif Banco.opcoes == 3:
        Banco.sacar()
        break
    elif Banco.opcoes == 4:
        Banco.total_restante()
        break
    elif Banco.opcoes == 5:
        Banco.deseja_continuar()
        break
"""