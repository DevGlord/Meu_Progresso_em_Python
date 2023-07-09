# isinstance

lista = [
    'a', 1,1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome':'Luiz'},
]

for item in lista:
    
    if isinstance(item, set):
        print('SET')
        item.add(10)
        print(item)
        
    elif isinstance(item, dict):
        print('DICT')
        item.values()
        print(item,isinstance(item, dict)) # desse jeito é que retornará true or false!!!
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper())
    
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
        
    elif isinstance(item, list):
        print('LISTA')
        print(item)
    
    elif isinstance(item, tuple):
        print('TUPLA')
        print(item)   
    else:
        print('Outro')
        print(item)