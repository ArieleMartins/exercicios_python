import requests
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

moedas = requests.get()