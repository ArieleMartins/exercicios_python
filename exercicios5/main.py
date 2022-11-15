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

for interval in range(1, 500):
    if interval % 3 == 0:
        print(interval)

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










