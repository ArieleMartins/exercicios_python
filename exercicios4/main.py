#EMPRESTIMO

'''

print('\033[1:35m*=*\033[m' * 20)
print('Emprestimo')
print('\033[1:35m*=*\033[m' * 20)

casa = input('Digite o valor da casa: ')
salario = input('Digite seu salario: ')
anos = input('Em quantos anos você pretente pagar: ')

while casa.isnumeric() == False and salario.isnumeric() == False and anos.isnumeric() == False:
    print('Por favor digite um numero')
    casa = input('Digite o valor da casa: ')
    salario = input('Digite seu salario: ')
    anos = input('Em quantos anos você pretente pagar: ')
else:
    valorMes = float(casa) / (float(anos) * 12)
    porcentoSalario = (float(valorMes) * 100) / float(salario)

    if porcentoSalario > 30:
        print('Você não poderá fazer o emprestimos, pois passa de 30% do seu salario. Porcento: {}'.format(porcentoSalario))
    else:
        print('PARABÉNS!!! SEU EMPRESTIMO FOI ACEITO. Porcento: {}'.format(porcentoSalario))



'''

'''

numero = input('Digite um numero: ')

while numero.isnumeric() == False:
    print('Por favor digite um numero')
    numero = input('Digite um numero: ')
else:
    

'''

#MAIOR E MENOR

'''

n1 = input("Digite um numero: ")
n2 = input("Digite outro numero: ")

while n1.isnumeric() == False and n2.isnumeric() == False:
    print("Por favor digite somente numeros")
    n1 = input("Digite um numero: ")
    n2 = input("Digite outro numero: ")
else:
    if int(n1) > int(n2):
        print('{} é maior que {}'.format(n1, n2))
    elif int(n2) > int(n1):
        print('{} é maior que {}'.format(n2, n1))
    else:
        print('Os valores são iguais')

'''

#ALISTAMENTO

'''

import datetime

anoNasc = input('Digite o seu ano de nascimento: ')

while anoNasc.isnumeric() == False:
    print('Por favor digite somente numeros')
    anoNasc = input('Digite o seu ano de nascimento: ')
else:
    anoAtual = datetime.date.today().year
    idade = anoAtual - int(anoNasc)
    if idade == 18:
        print("Você deve se alistar")
    elif idade > 18:
        print('Já passo da hora de você se alistar')
        passo = idade - 18
        print('Passou {} anos do pedido para se alistar'.format(passo))
    else:
        falta = 18 - idade
        print('Você ainda vai se alistar')
        print('Falta {} anos para você se alistar'.format(falta))

'''

#MEDIA

'''

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

while nota1.isnumeric() == False and nota2.isnumeric() == False:
    print("Por favor digite somente numeros")
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
else:
    media = (float(nota1) + float(nota2)) / 2
    print("\033[0:35m-=-\033[m" * 10)
    if media  < 5:

        print('\033[0:31mREPROVADO\033[m')
    elif media > 5 and media < 6.9:
        print("\033[0:34mRECUPERAÇÃO\033[m")
    else:
        print("\033[0:32mAPROVADO\033[m")
    print("\033[0:35m-=-\033[m" * 10)

'''

#CATEGORIA NATACAO

'''

import datetime

print("\033[0:35m-=-\033[m" * 12)
print("CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("\033[0:35m-=-\033[m" * 12)

anoNasc = input('Digite seu ano de nascimento: ')

while anoNasc.isnumeric() == False:
    print("Por favor digite somente numero")
    anoNasc = input('Digite seu ano de nascimento: ')
else:
    idade = datetime.date.today().year - int(anoNasc)

    if idade <= 9:
        print("CATEGORIA: MIRIM")
    elif idade > 9 and idade <= 14:
        print("CATEGORIA: INFANTIL")
    elif idade > 14 and idade <= 19:
        print("CATEGORIA: JUNIOR")
    elif idade == 20:
        print("CATEGORIA: SÊNIOR")
    else:
        print("CATEGORIA: MASTER")

'''

#TRIANGULO

'''

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
    if r1 == r2 and r2 == r3 and r1 == r3:
        print('Equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não pode formar um triangulo')

'''

#IMC

'''

print("\033[0:35m-=-\033[m" * 12)
print("CALCULANDO IMC")
print("\033[0:35m-=-\033[m" * 12)

altura = input("Digite sua altura: ")
peso = input("Digite seu peso: ")

while altura.isnumeric() == False and peso.isnumeric() == False:
    print('Por favor digite somente numeros')
    altura = input("Digite sua altura: ")
    peso = input("Digite seu peso: ")
else:
    imc = float(peso) / (float(altura.replace(',', '.')) * float(altura.replace(',', '.')))
    if imc < 18.5:
        print("Você esta abaixo do peso. IMC: {:.2f}".format(imc))
    elif imc >= 18.5 and imc <= 25:
        print("Você esta no peso ideal. IMC: {:.2f}".format(imc))
    elif imc > 25 and imc <= 30:
        print("Você esta com sobrepeso. IMC: {:.2f}".format(imc))
    elif imc > 30 and imc <= 40:
        print("Você esta com obesidade. IMC: {:.2f}".format(imc))
    else:
        print("Você esta com obesidade mórbida. IMC: {:.2f}".format(imc))

'''

#JOKENPÔ

'''

import random

player = ''
bot = random.randint(0, 2)
ganhador = ''

def printJogadas():
    print('0 - Tesoura')
    print('1 - Papel')
    print('2 - Pedra')

def identJogada(jogada):
    jog = ["Tesoura", 'Papel', 'Pedra']
    return jog[jogada]
def Jogar():
    verifGanhador = False
    jogadas = [
        ['0', '1', "PLAYER"],
        ["1", "0", 'MÁQUINA'],
        ['0', '2', 'MÁQUINA'],
        ['2', '0', 'PLAYER'],
        ['1', '2', 'PLAYER'],
        ['2', '1', 'MÁQUINA']
    ]

    for i in range(len(jogadas)):
        if jogadas[i][0] in player:
            if jogadas[i][1] in str(bot):
                verifGanhador = True
                ganhador = jogadas[i][2]

    if verifGanhador == True:
        print('-=-' * 10)
        print("\033[0:35mMÁQUINA:\033[m {}".format(identJogada(bot)))
        print('\033[0:34mPLAYER:\033[m {}'.format(identJogada(int(player))))
        print('-=-'* 10)
        print('\033[0:32mGANHADOR É {}\033[m '.format(ganhador))
        print('-=-' * 10)
    else:
        print('-=-' * 10)
        print("\033[0:35mMÁQUINA:\033[m {}".format(identJogada(bot)))
        print('\033[0:34mPLAYER:\033[m {}'.format(identJogada(int(player))))
        print('-=-' * 10)
        print("\033[0:34mEMPATE\033[m")




print("\033[0:35m-=-\033[m" * 10)
print("{}JOKENPÔ{}".format(' ' * 11, ' ' * 11))
print("\033[0:35m-=-\033[m" * 10)

printJogadas()

player = input('Digite sua jogada: ')

while player != "0" and player != "1" and player != "2":
    printJogadas()
    print('\033[0:31mDigite um dos numeros acima\033[m')
    player = input('Digite sua jogada: ')
else:
    Jogar()

'''

