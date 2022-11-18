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
