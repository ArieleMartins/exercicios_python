import math

#ceil - arredonda para cima
#floor - arredonda para baixo
#trunc - elimina da virgula para frente
#pow - potencia
#sqrt - raiz quadrada
#factorial - calculo de fatorial
#
'''
valor= input('digite um numero')
if valor.replace('.','').isnumeric():
    inteiro = math.floor(float(valor))
    print(inteiro)
'''

import random
import os
#gerar numeros aleatorios entre 0 e 1
# random.random de 0 e 1
# random.randint() - você escolhe os numero, por exemplo: entre 5 e 20. Somente sairá os valores igual ou a cima de 5 e igual ou abaixo de 20
#valor = random.randint(1, 10)
#print(valor)
'''
nomes = []
pausar = 'S'
while pausar.upper() == "S":
    nome = input('Digite o nome do aluno que irá participar: ')
    nomes.append(nome)
    pausar = input('Deseja adicionar mais alunos? s/n')
else:
    aluno = nomes[random.randint(0, len(nomes) - 1)]
    print('O aluno escolhido foi {}'.format(aluno))
'''
'''
nomes = []
ordem = []
pausar = 'S'
while pausar.upper() == "S":
    nome = input('Digite o nome do aluno que irá participar: ')
    nomes.append(nome)
    pausar = input('Deseja adicionar mais alunos? s/n')
else:
    ordem = random.sample(range(len(nomes)), len(nomes)) #para que não repeti o mesmo numero

i = 1
for n in ordem:
    print("Quem irá apresentar em {} é: {}".format(i, nomes[n]))
    i = i + 1
'''

'''
valor = input("Digite algo: ")
primitivo = type(valor)
space = valor.isspace()
number = valor.isnumeric()
alfabetico = valor.isalpha()
alfanumerico = valor.isalnum()
minusculo = valor.islower()
maiusculo = valor.isupper()
capitalizado = valor.istitle()

print("O tipo primitivo desse valor é: {}\nSó tem espaços? {}\nÉ um número? {}\nÉ alfabético? {}\nÉ alfanúmerico? {}\nEstá em maiusculo? {}\nEsta em minusculo? {}\nEsta capitalizada? {}".format(primitivo, space, number, alfabetico, alfanumerico,maiusculo, minusculo, capitalizado))
'''

#Operadores Aritméticos
#Adição _ +
#Subtração _ -
#multiplicação _ *
#divisão _ /
#potencia _ **
#divisão inteira _ //
#resto da divisão _ %

# Exercicio Antecessor e Sucessor
'''
valor = input("Digite um número: ")
while valor.isnumeric() == False:
    valor = input("Digite um número: ")
else:
    antecessor = int(valor) - 1
    sucessor = int(valor) + 1
    print('O antecessor de {} é {} e o sucessor é {}'.format(valor, antecessor, sucessor))
'''
# Exercicio Média
'''
pausar = "S"

contador = 0
notas = []
soma = 0
while pausar.upper() == "S":
    nota = input('Digite a nota:\n Nota {}: '.format(contador))
    if nota.isnumeric():
        notas.append(float(nota))
        contador = contador + 1
        pausar = input('Tem mais notas para adicionar? s/n')
    else:
        print('Por favor digite um número')
else:
    for n in notas:
        soma = soma + n
    media = soma / len(notas)
    print('A média é {}'.format(media))
'''

#converte metro por milimetro e centimetros
'''
metro = input('digite o metro: \n')
if metro.isnumeric():
    convertCent = int(metro) * 100
    convertMili = int(metro) * 1000
    print('O metro {} em centimetro é {} e em milimetro é {}'.format(metro, convertCent, convertMili))
else:
    print('Por favor digite um numero')
'''

#Tabuada
'''
numero = input('Digite um numero: ')
contador = 0
if numero.isnumeric():
    while contador < 11:
        print('{} X {} = {}'.format(numero, contador , contador*int(numero)))
        contador = contador + 1
else:
    print('Por favor digite um numero')
'''

#Calculo de Area
'''
altura = input('Digite a altura da parede: ')
largura = input('Digite a largura da parede: ')
if altura.replace('.', '').isnumeric() and largura.replace('.','').isnumeric():
    area = float(altura) * float(largura)
    tinta = area / 2
    print('A quantidade de tinta que será usanda é {}'.format(int(tinta)))
else:
    print('por favor digite somente numeros')
'''

#desconto
'''
valor = input('Digite o valor do produto: ')
if valor.replace('.', '').isnumeric():
    desconto = (float(valor) * 12) / 100
    valorDescontado = float(valor) - desconto
    print('Com o desconto de 12% o valor vai para {}'.format(valorDescontado))
else:
    print('Por favor digite somente números')
'''
#aumento de salario
'''
salario = input('Digite seu salario: ')
if salario.replace('.','').isnumeric():
    aumento = (float(salario) * 15)/100
    salarioAumentado = float(salario) + aumento
    print('Com 15% de aumento seu salario irá para {}'.format(salarioAumentado))
else:
    print("Por favor digite somente numeros")
'''