# aprendendo tuplas

number = input('Digite um número de 0 a 20: ')

while number.isnumeric() == False or int(number) < 0 or int(number) > 20:
    number = input("Digite um número de 0 a 20: ")
else:
    numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(f'Você digitou o número {numbers[int(number)]}')

