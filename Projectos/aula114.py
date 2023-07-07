"""
from sys import path

import aula114_package.modulo
from aula114_package.modulo import soma_do_modulo
from aula114_package import modulo
from aula114_package.modulo import *

print(*path, sep='\n')
print(soma_do_modulo(10, 19))
print(aula114_package.modulo.soma_do_modulo(10, 19))
print(soma_do_modulo(10, 19))
print(variavel)
"""
print(__name__)

from aula114_package import soma_do_modulo

print(soma_do_modulo(10, 2))


