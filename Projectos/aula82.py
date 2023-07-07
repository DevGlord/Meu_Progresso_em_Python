# 128. Métodos úteis do tipo set em Python

s1 = set()
s1.add('Maximiano')
s1.add(1)
s1.update(('Olá mundo',1,2,3))
s1.update('Olá mundo')
#s1.clear()
s1.discard('Olá mundo')
print(s1)
