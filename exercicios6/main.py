# PRATICANDO WHILE

'''

sexo = input("Digite seu sexo: [M/F] ")
while sexo.upper() != 'M' and sexo.upper() != 'F':
    print('Por favor digite M ou F')
    sexo = input("Digite seu sexo: [M/F] ")
else:
    print('O seu sexo é {}'.format(sexo))

'''

#ADIVINHAÇÃO

'''

import random

bot = random.randint(0, 10)

player = input('Qual é o numero que a maquina pensou: ')

while player.isnumeric() == False:
    print('Por favor digite somente numeros')
    player = input('Qual é o numero que a maquina pensou: ')
else:
    while int(player) != bot:
        print('Você errou, tente novamente')
        player = input('Qual é o numero que a maquina pensou: ')
    else:
        print('PARABÉNS!! VOCÊ ACERTOU')

'''

# QUASE UMA CALCULADORA

'''

num1 = input("Digite o primeiro numero: ")
num2 = input('Digite o segundo numero: ')
opcao = '0'

while opcao != '5':
    while num1.isnumeric() == False and num2.isnumeric() == False:
        print('Por favor digite somente numeros')
        num1 = input("Digite o primeiro numero: ")
        num2 = input('Digite o segundo numero: ')
    else:
        print('Qual a operação que deseja realizar')
        print('[1] SOMA')
        print('[2] MULTIPLICAÇÃO')
        print('[3] MAIOR')
        print('[4] NOVOS NUMEROS')
        print('[5] sair do programa')
        opcao = input('Digite uma da opcoes: ')
        while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
            print('Por favor digite uma das opcoes abaixo')
            print('[1] SOMA')
            print('[2] MULTIPLICAÇÃO')
            print('[3] MAIOR')
            print('[4] NOVOS NUMEROS')
            print('[5] sair do programa')
            opcao = input('Digite uma da opcoes: ')
        else:
            if opcao == '1':
                soma = int(num1) + int(num2)
                print('A soma dos numero é {}'.format(soma))
            elif opcao == '2':
                multiplicacao = int(num1) * int(num2)
                print('a multiplicacao dos numeros é {}'.format(multiplicacao))
            elif opcao == '3':
                if num1 > num2:
                    maior = num1
                    print('O maior numero é {}'.format(maior))
                elif num2 > num1:
                    maior = num2
                    print('O maior numero é {}'.format(maior))
                else:
                    print('Os numero sao iguais')
            elif opcao == '4':
                num1 = input("Digite o primeiro numero: ")
                num2 = input('Digite o segundo numero: ')

'''


# FATORIA

'''

num = input('Digite um numero: ')

mult = 1

while num.isnumeric() == False:
    print('Por favor digite somente numeros')
    num = input('Digite um numero: ')
else:
    contador = int(num)
    while contador != 0:
        mult = mult * contador
        contador -= 1
    else:
        print('O valor fatorial do numero é {}'.format(mult))

'''

#PROGRESSÃO ARITMETICA

'''

primeiro = input('Digite o primeiro termo: ')
razao = input('Digite a razao: ')
decimo = int(primeiro) + (10 - 1) * int(razao)
for interval in range(int(primeiro), int(decimo) + int(razao), int(razao)):
    print("{}".format(interval))
print('===' * 10)
pula = int(primeiro)
while pula <= decimo:
    print(pula)
    pula = pula + int(razao)

'''









