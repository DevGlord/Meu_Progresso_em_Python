# Try, except, else e finally parte 1 e 2


try:
    a = '10'
    b = '0'
    c = a / b

except Exception as e: # no lugar do "e" pode ficar la qualquer coisa
    print('MSG:',e)
    print('Nome',e.__class__.__name__)
    print(e)

else:
    print(c)
