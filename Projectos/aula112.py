try:
    import sys
    sys.path.append('/home')
    
    #import aula106
except ModuleNotFoundError:
    ...

print(*sys.path,sep='\n')

