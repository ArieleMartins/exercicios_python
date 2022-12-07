# aprendendo tuplas


'''

number = input('Digite um número de 0 a 20: ')

while number.isnumeric() == False or int(number) < 0 or int(number) > 20:
    number = input("Digite um número de 0 a 20: ")
else:
    numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(f'Você digitou o número {numbers[int(number)]}')

'''

# TABELA DO BRASILEIRÃO

'''

classificacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Amérca-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Os cinco primeiros colocados: \n{classificacao[0:6]}')
print(f'Os ultimo 4 colocados: \n{classificacao[16:21]}')
print(f'{sorted(classificacao)}')
print(f'O Atlético-MG está na posicao {classificacao.index("Atlético-MG")}')

'''



