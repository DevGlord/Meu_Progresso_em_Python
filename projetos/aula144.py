from copy import deepcopy
import os
import json

def mostrar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas:')
    
    for tarefa in tarefas:
        print(f'\t->{tarefa}<-')

def desfazer(tarefas,tarefas_desfazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas')
    tarefas_desfazer.append(tarefa)
    print()
    mostrar(tarefas)
    print()
    
    
def refazer(tarefas,tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    
    
def adicionar(tarefa,tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma tarefa para adicionar.')
        return
    tarefas.append(tarefa)

def ler(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo,'r',encoding='uf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados
    
    
def salvar(tarefas,caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo,'w',encoding='utf8') as arquivo:
        dados = json.dump(tarefas,arquivo,indent=2,ensure_ascii= False)
    return dados



CAMINHO_ARQUIVO = 'aula144.json'


    
tarefas = []
tarefas_refazer = []

while True: 
       
    print('''Escolhe a melhor opção para você!
        [adicionar]
        [desfazer]          
        [refazer]
        [cls]
        [mostrar]
    ''') 

    tarefa = input('A sua opção é:')

    comandos = {
        "adicionar":lambda: adicionar(tarefa, tarefas),
        "desfazer": lambda: desfazer(tarefas,tarefas_refazer),
        "refazer": lambda: refazer(tarefas, tarefas_refazer),
        "cls": lambda: os.system('cls'),
        "mostrar":lambda:mostrar(tarefas),
        }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar'] 
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)



    
"""        
    if tarefa == "DESFAZER":
        desfazer(tarefas, tarefas_refazer)
    
    elif tarefa == "REFAZER":
        refazer(tarefas, tarefas_refazer)
           
    elif tarefa == "APAGAR TUDO":
        os.system('cls')
        
    elif tarefa == "MOSTRAR":
        mostrar(tarefas)
        
    elif tarefa == "SAIR":
        print('Programa encerrado!')
        break
    else:
        adicionar(tarefa, tarefas)
"""        

        