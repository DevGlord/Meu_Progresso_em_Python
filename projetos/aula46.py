for i in range(10):
    if i == 2:
        print('O i pulou o 2.')
        continue
    #if i == 8:
        #print('O for não foi completo.')
        #break
    for j in range(1,3):
        print(i,j)
else:
    print('O for foi completado')