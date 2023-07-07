# Modulos padrão do Python (import, from, as e *)
"""
import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)
"""

#from sys import exit, platform
#print(platform)

"""
import sys as s
sys = 'alguma coisa'
print(s.platform)
print(sys)
"""
"""
from sys import platform as pf, exit as ex
print(pf)
"""

from sys import *

print(platform)
exit()
