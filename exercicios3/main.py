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
