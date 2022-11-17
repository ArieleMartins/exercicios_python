# APRENDENDO A USAR BREAK

'''

number = input('Digite um numero: ')
count = sum = 0
while number.isnumeric() == False:
    print('Por favor digite somente números')
    number = input('Digite um numero: ')
else:
    while True:
        sum += int(number)
        count += 1
        number = input('Digite um numero: ')
        if number == '999':
            break
print(f'Você digite o total de {count} números e a soma entre ele é {sum}')

'''


