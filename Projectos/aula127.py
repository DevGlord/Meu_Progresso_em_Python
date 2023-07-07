"""
from itertools import count
x = count(10)
for v in x:
    print(v)
    break
"""
"""
from itertools import cycle
x = cycle('abc')
for v in x:
    print(v)
"""
"""
from itertools import repeat
x = repeat('10',3)
for v in x:
    print(v)
"""

from itertools import accumulate

x = accumulate([1,2,3,4,5])
# or x = list(accumulate([1,2,3,4,5])) # output: [1,3,6,10,15]
#print(list(x))
"""
r = accumulate([i for i in range(0,100)])
print(list(r))
for v in x:
    print(v)
"""
"""
from itertools import chain

x = chain('caio',[1,2,3])

for v in x:
    print(v)
"""
"""
from itertools import compress

x = compress([1,2,3,4],[1,0,0,1])
print(list(x))
"""
from itertools import product

x = [1,2,3,4,5],[1,2,3,4,5,6]
v = list(product(x))
for c in v:
    print(c)