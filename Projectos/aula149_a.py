from aula149 import LOCAL_ARQUIVO, Pessoa,fazendo_dump
import json


fazendo_dump()

with open(LOCAL_ARQUIVO,'r',encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    cas = Pessoa(**dados[0])
    print(cas.nome)
