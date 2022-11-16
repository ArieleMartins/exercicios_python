#CONTAGEM

'''

import time

print("\033[0:31m-*-\033[m" * 10)
print("\033[0:32m{:^30}\033[m".format("FELIZ ANO NOVO"))
print("\033[0:31m-*-\033[m" * 10)

print('E QUE COMECE A CONTAGEM')

for interval in range(10, 0, -1):
    print("{} !!!".format(interval))
    time.sleep(1)
print("\033[0:31m-*-\033[m" * 10)
print("\033[0:32m{:^30}\033[m".format("FELIZ ANO NOVO !!!!!"))
print("\033[0:31m-*-\033[m" * 10)

'''

#PARES ENTRE 1 E 50

'''

for interval in range(1, 50):
    if interval % 2 == 0:
        print(interval)

'''

#NUMERO IMPARES MULTIPLOS DE TRES


'''

soma = 0

for interval in range(1, 501, 2):
    if interval % 3 == 0:
        soma = soma + interval
print('A soma de todos os numero impare é {}'.format(soma))

'''




#TABUADA

'''

numero = input('Digite o numero que deseja ver a tabuada: ')

while numero.isnumeric() == False:
    print('Por favor digite somente numeros')
    numero = input('Digite o numero que deseja ver a tabuada: ')
else:
    for interval in range(0, 11):
        tabuada = int(numero) * interval
        print('{} X {} = {}'.format(interval, numero, tabuada))

'''


#SOMA DE NUMEROS PARES

'''

soma = 0

for interval in range(0, 6):
    numero = input('Digite um numero: ')
    if int(numero) % 2 == 0:
        soma = soma + int(numero)

print("A soma dos numero pares é {}".format(soma))

'''

#NUMERO PRIMO

'''

numero = input("Digite um numero: ")

while numero.isnumeric() == False:
    print('Por favor digite somente numeros ')
    numero = input("Digite um numero: ")
else:
    if int(numero) % 1 == 0 and int(numero) % int(numero) == 0:
        print('É um numero primo')
    else:
        print('Não é um numeor primo')

'''

#PALÍNDROMO

'''

frase = input('Digite uma frase: ')

fraseSemEspaco = frase.replace(' ', '')

novaFrase = ''

for interval in range(len(fraseSemEspaco) - 1, -1, -1):
    novaFrase += fraseSemEspaco[interval]

if novaFrase == fraseSemEspaco:
    print("É um PALINDROMO")
else:
    print("Não é um PALINDROMO")

'''

#MAIORES E MENORES DE IDADE


'''

import datetime

ano = []
maiores = 0
menores = 0

for interval  in range(1, 8):
    nasc = input('Digite o ano de nascimento da {} pessoa: '.format(interval))

    while nasc.isnumeric() == False:
        print('Por favor digite somente numeros')
        nasc = input('Digite o ano de nascimento da {} pessoa: '.format(interval))
    else:
        ano.append(int(nasc))

for interv in range(0, len(ano)):
    if (datetime.date.today().year - ano[interv]) >= 18:
        maiores += 1
    else:
        menores += 1

print('Tem {} maiores de idade e {} menores de idade'.format(maiores, menores))

'''

#MAIOR E MENOR PESO

'''

pesos = []

for interval in range(1, 6):
    peso = input('Digite o peso da {} pessoa: '.format(interval))
    while peso.isnumeric() == False:
        print('Por favor digite somente numeros')
        peso = input('Digite o peso da {} pessoa: '.format(interval))
    else:
        pesos.append(float(peso))

pesos.sort()

maior = pesos[len(pesos) - 1]
menor = pesos[0]

print('O maior peso é {} e o menor é {}'.format(maior, menor))

'''


#MÉDIA E IDADE

'''

soma = 0
velho = 0
nomeVelho = ''
novas = 0
for interval in range(1, 5):
    nome = input("Digite o nome da {} pessoa: ".format(interval))
    idade = input("Digite a idade da {} pessoa: ".format(interval))

    while idade.isnumeric() == False:
        print("Por favor digite somente numeros: ")
        idade = input("Digite a idade da {} pessoa: ".format(interval))
    else:
        sexo = input("Digite o sexo da {} pessoa: F ou M ".format(interval))

        while sexo.upper() != "F" and sexo.upper() != "M":
            print('Por favor digite F ou M')
            sexo = input("Digite o sexo da {} pessoa: F ou M ".format(interval))
        else:
            soma += soma + int(idade)
            if interval == 1 and sexo.upper() == "M":
                velho = int(idade)
                nomeVelho = nome
            elif sexo.upper() == "M" and int(idade) > velho:
                velho = int(idade)
                nomeVelho = nome
            if sexo.upper() == "F" and int(idade) < 20:
                novas += 1

media = soma / 4
print("A idade media do grupo é {}".format(media))
print("O homem mais velho tem {} e se chama {}".format(velho, nomeVelho))
print("A quantidade de mulheres menos de 20 anos é {}".format(novas))

'''

#PROGRESSÃO ARITMETICA

'''

primeiro = input('Digite o primeiro termo: ')
razao = input('Digite a razao: ')
decimo = int(primeiro) + (10 - 1) * int(razao)
for interval in range(int(primeiro), int(decimo) + int(razao), int(razao)):
    print("{}".format(interval))

'''
