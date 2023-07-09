
def soma(parametro):
    def resultado(x,y):
        res = x + y
        return parametro(res)
    return resultado

@soma


def msg(mensagem):
    return f'O resultado é {mensagem}'

v = msg(10, 20)
print(v)



