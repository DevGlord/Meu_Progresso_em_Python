import importlib
import aula113m

print(aula113m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula113m)
    print(i)

print('FIM')