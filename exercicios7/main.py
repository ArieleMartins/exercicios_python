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

# tabuada

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


