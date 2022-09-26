import requests
import json
#Conversor de moeda
requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
resposta = requisicao.json()
real = input('Digite o valor em real: ')
if real.replace('.','').isnumeric():
    convert = float(real) * float(resposta['USDBRL']['bid'])
    print(convert)


