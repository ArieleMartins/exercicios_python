'''

JOGO ADIVINHAÇÃO

import random
tentar = 'S'
print("Adivinha qual o  numero que a maquina penso de 0 a 5")
while tentar == 'S':
    bot = random.randint(0, 5)
    user = input('Qual é o número que a máquina pensou? ')
    while user.isnumeric() == False:
        print('Por favor digite um numero')
        user = input('Qual é o número que a máquina pensou? ')
    else:
        if int(user) == bot:
            print('PARABENS VOCÊ ACERTOU')
            tentar = input('Gostaria de tentar de novo?')
        else:
            print('VOCÊ ERROU')
            tentar = input('Gostaria de tentar de novo?')
else:
    print('Obrigada por jogar :)')

'''

'''

VELOCIDADE E MULTA

velocidade = input('Digite a velocidade do carro: ')

while velocidade.isnumeric() == False:
    print('Por favor digite um numero')
    velocidade = input('Digite a velocidade do carro: ')
else:
    if int(velocidade) > 80:
        print('Você receberá uma multa')
        multa = (int(velocidade) - 80) * 7
        print('O valor da multa é de R${}'.format(multa))
    else:
        print('Parabens não irá receber multa')


'''

'''

VALOR DA PASSAGEM POR QUILOMETRO

distancia = input('Qual é a distancia da viagem? ')
while distancia.isnumeric() == False:
    print('Por favor digite um numero')
    distancia = input('Qual é a distancia da viagem? ')
else:
    if int(distancia) <= 200:
        valor = int(distancia) * 0.50
        print('Valor da passagem é R${}'.format(valor))
    else:
        valor = int(distancia) * 0.45
        print('Valor da passagem é R${}'.format(valor))


'''


'''

ORDEM CRESCENTE

num1 = input("Digite um numero: ")
num2 = input('Digite mais um numero: ')
num3 = input('Digite o ultimo numero: ')

while num1.isnumeric() == False or num2.isnumeric() == False or num3.isnumeric() == False :
    print('Por favor digite um numero')
    num1 = input("Digite um numero: ")
    num2 = input('Digite mais um numero: ')
    num3 = input('Digite o ultimo numero: ')
else:
    n1 = int(num1)
    n2 = int(num2)
    n3 = int(num3)
    if n1 > n2 and n1 > n3:
        maior = n1
        if n2 > n3:
            medio = n2
            menor = n3
        else:
            medio = n3
            menor = n2
    elif n2 > n1 and n2 > n3:
        maior = n2
        if n3 > n1:
            medio = n3
            menor = n1
        else:
            medio = n1
            menor = n3
    elif n3 > n1 and n3 > n2:
        maior = n3
        if n1 > n2:
            medio = n1
            menor = n2
        else:
            medio = n2
            menor = n1
    print('{}   {}    {}'.format(maior, medio, menor))

'''

'''

AUMENTO DE SALARIO

salario = input('Digite seu salario: ')

while salario.isnumeric() == False:
    print("Por favor digite um numero")
    salario = input('Digite seu salario: ')
else:
    if int(salario) > 1250:
        aumento = ((int(salario) * 10) / 100) + int(salario)
        print('Seu salario aumentou para {}'.format(aumento))
    else:
        aumento = (((int(salario)) * 15) / 100) + int(salario)
        print('Seu salario aumentou para {}'.format(aumento))
'''

'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 18)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO....')
sleep(3)
if int(jogador) == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

'''

'''

ÌMPAR OU PAR

numero = input('Digite um numero: ')

while numero.isnumeric() == False:
    print('Por favor digite um numero')
    numero = input('Digite um numero: ')
else:
    if int(numero) % 2 == 0:
        print("Número Par")
    else:
        print('Número Ímpar')
'''

'''

import datetime


ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual \n"))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))

'''

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')