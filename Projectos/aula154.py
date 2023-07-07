class animal:
    @staticmethod
    def nomes(nome, *args, **kwargs):
        print(args, kwargs)
        
animal.nomes('Max',1,2,3,nomes = '1')     