# APRENDENDO A USAR BREAK

'''

number = input('Digite um numero: (999 para parar)')
count = sum = 0
while number.isnumeric() == False:
    print('Por favor digite somente números')
    number = input('Digite um numero: (999 para parar)')
else:
    while True:
        sum += int(number)
        count += 1
        number = input('Digite um numero: (999 para parar)')
        if number == '999':
            break
print(f'Você digite o total de {count} números e a soma entre ele é {sum}')

'''

# TABUADA

'''

number = input("Deseja ver a tabuade de qual valor? (valor negativo para parar) ")
count = 0
while number.isnumeric() == False:
    print('Por favor digite somente numeros')
    number = input("Deseja ver a tabuade de qual valor? (valor negativo para parar)")
else:
    while True:
        while True:
            print(f'{count} X {number} = {count * int(number)}')
            count += 1
            if count == 11:
                break
        number = input("Deseja ver a tabuade de qual valor? (valor negativo para parar)")
        count = 0
        if int(number) < 0:
            break

'''

#JOGO IMPAR OU PAR

'''

import random

print('=-' * 10)
print('ÍMPAR OU PAR')
print('=-' * 10)

number = 1
while int(number) != '0':
    bot = random.randint(0, 10)
    number = input('Diga o valor:')
    while number.isnumeric() == False:
        print('Por favor digite somente números')
        number = input('Diga o valor: ')
    else:
        option = input('Par ou Ímpar: [P/I] ')
        while option.upper() != "P" and option.upper() != "I":
            print("Por favor digite P ou I")
            option = input('Par ou Ímpar: [P/I] ')
        else:
            sum = bot + int(number)
            if sum % 2 == 0:
                if option.upper() == 'P':
                    print('Você ganhou')
                else:
                    print('A máquina ganhou')
            else:
                break

print('Você perdeu')

'''


'''

totalMaior = 0
totalMulherMenor = 0
totalHomem = 0
opcao = 'S'


while True:
    idade = input('Digite a idade: ')
    while idade.isnumeric() == False:
        print('Por favor digite somente números')
        idade = input('Digite a idade: ')
    else:
        sexo = input('Digite o sexo: ')
        while sexo.upper() != 'F' and sexo.upper() != "M":
            print('Por favor digite F ou M')
            sexo = input('Digite o sexo: [F/M]')
        else:
            if int(idade) >= 18:
                totalMaior += 1
            elif int(idade) < 18:
                if sexo.upper() == "F":
                    totalMulherMenor += 1
            if sexo.upper() == 'M':
                totalHomem += 1
    opcao = input('Você deseja continuar? [S para continuar]')
    if opcao.upper() != "S":
        break
print(f'Maiores de idade: {totalMaior}')
print(f'Homens: {totalHomem}')
print(f'Mulheres menores: {totalMulherMenor}')

'''

'''

totalGasto = 0
caro = 0
maisBarato = 0
nomeBarato = ''
count = 0
while True:
    produto = input("Digite o nome do produto: ")
    valor = input('Digite o valor do produto: ')
    while valor.replace('.', '').isnumeric() == False:
        print('Por favor digite somente numeros')
        valor = input('Digite o valor do produto: ')
    else:
        totalGasto += float(valor.replace(',', '.'))
        if float(valor.replace(',', '.')) > 1000:
            caro += 1
        if count == 0:
            maisBarato = float(valor.replace(',', '.'))
            nomeBarato = produto
        elif maisBarato > float(valor.replace(',', '.')):
            maisBarato = float(valor.replace(',', '.'))
            nomeBarato = produto
        count += 1
    opcao = input('Deseja continuar? [S/N]')
    while opcao.upper() != "S" and opcao.upper() != "N":
        opcao = input('Deseja continuar? [S/N]')
    else:
        if opcao.upper() == 'N':
            break
print(f'Total Gasto: {totalGasto}')
print(f'Quantidade de produtos que custam mais de 1000: {caro}')
print(f'Produto mais barato: {nomeBarato}')

'''
