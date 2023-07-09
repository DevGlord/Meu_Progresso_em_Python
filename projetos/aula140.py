import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)
#print(requisicao.json())

dic_requisicao = requisicao.json()
print(dic_requisicao)
print(f'A cotação do dolar está ${dic_requisicao ["USDBRL"]["bid"] }')

print(dic_requisicao)

