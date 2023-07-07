
def generator(n= 0,maximum = 10):
    """
    yield 1# pausar
    print('continuado...')
    yield 2 #pausar
    print('Vou terminar...')
    yield 3
    return 'Acabou'
    """
    while True:
        yield n
        
        n += 1
        if n >= maximum:
            return
    
gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#for n in gen:
    #print(n)
