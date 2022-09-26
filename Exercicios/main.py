# format para adicionar o valor da variavel no texto usando chaves
# int para converter os dados em inteiros
#isnumeric - verifica se é possivel converter aquele valor em um tipo numerico
# criando uma matriz
cardapio = [['Codigo', 'Produto', 'Valor'], ['100', 'Hambuguer', 'R$ 6,00'], ['101', 'X-Salada', 'R$ 8,00'],
            ['102', 'X-Bacon', 'R$ 10,00'], ['103', 'Refrigerante', 'R$ 2,50'], ['104', 'X-Tudo', 'R$ 12,00'],
            ['105', 'Café', 'R$ 4,00']]  # matriz
add = 0  # variavel onde ficara a quantidade de espaço - col 1
addcod = 0  # variavel onde ficara a quantidade de espaço -  col 0
print("--------***Cardapio***--------")
for itens in cardapio:
    espcod = len(itens[0])  # pegando a quantidade de caracteres na variavel itens col 0
    esp = len(itens[1])  # pegando a quantidade de caracteres na variavel itens col 1
    if (esp < 12):  # verificando se o valor obtido é menor que 12
        if (
                esp != 12):  # se o valor for diferente de 12 faça, não é necessaria essa parte, só para ter certeza que é diferente de 12
            add = 13 - len(itens[
                               1])  # pegue a quantidade de caracteres menos 13 (que é a maior palavra que tem "refrigerante", porém adicionado mais um)
    if (esp == 12):  # se o valor obtido for igual a 12 faça
        add = 1  # adicione somente 1

    if (espcod < 6):  # se o valor obtido for menor que 6 faça
        if (
                espcod != 6):  # se for diferente de 6 faça, não é necessaria essa parte, mas só para ter certeza que é diferente de 6
            addcod = 8 - len(
                itens[0])  # pegue a quantidade de caracteres que a variavel itens coluna 0 tem e faça menos 6
    if (espcod == 6):  # se a quantidade for igual a 6 faça
        addcod = 2  # adicione a variavel o valor 2
    print(itens[0] + ' ' * addcod + itens[1] + ' ' * add + itens[
        2])  # " ''*add " ele adiciona a quantidade de espaço de acordo com o valor da variavel add
codigo = input("Digite o código: ")

if (codigo == '100'):  # se
    quantidade = int(input("Digite a quantidade que deseja: "))  # convertendo string para numero inteiro
    print("Você pediu a quantidade de {}. Valor total a pagar: {}".format(quantidade, quantidade * 6.00))
elif (codigo == '102'):  # senão se
    quantidade = int(input("Digite a quantidade que deseja: "))
    print("Você pediu a quantidade de {}. Valor total a pagar: {}".format(quantidade, quantidade * 8.00))
elif (codigo == '103'):  # senão se
    quantidade = int(input("Digite a quantidade que deseja: "))
    print("Você pediu a quantidade de {}. Valor total a pagar: {}".format(quantidade, quantidade * 10.00))
elif (codigo == '104'):  # senão se
    quantidade = int(input("Digite a quantidade que deseja: "))
    print("Você pediu a quantidade de {}. Valor total a pagar: {}".format(quantidade, quantidade * 2.50))
elif (codigo == '105'):  # senão se
    quantidade = int(input("Digite a quantidade que deseja: "))
    print("Você pediu a quantidade de {}. Valor total a pagar: {}".format(quantidade, quantidade * 12.00))
else:  # senão
    print("Código Invalido")
    '''

# aprendendo a usar lista
#herois = ['Cavaleiro da Lua', 'Capitão America', 'Homem Aranha', 'Batman', 'Mulher Maravilha', 'Homem Formiga', 'Hulk',
#          'Deadpool', 'Homem Gelo']

#for i in herois:  # percorre toda a lista do array herois
#    print(i)

#dc = 'Batman'

#for i in dc:  # Ele percorre cada caracter da variavel
#    print(i)

#for i in range(0, 3):  # percorre o range de 0 até 2 - o ultimo não conta
#    print(herois[i])  # percorre o array da coluna 0 até a 2

# h = 'Cavalheiro da Lua'
"""
print(h[1]) #É como se cada caractere estivesse em um array , então ele exibirá o segundo caractere, porque o array começa com 0

print(h[0:10]) #ele pegará do 0 até o 8, pois o nove não contará - então o resultado será 'Cavalheiro'

if 'Lua' in h: # se na variavel encontrar a palavra lua - Ele percorre toda a variavel embusca da palavra 'lua' - Case sensitive - se substituir o in por not ele faz o inverso
    print('Encontrado') #execute
else: # se não encontrar
    print('Não Encontrado') #execute

print(len(h)) #exibir quantos caracteres possui a variavel
"""
# for numero in h: #exibi cada caracter da variavel
#    print(numero)

# test = [0,0,0],[0,0,0]
# col 0 - col 1
# print(len(test)) #conta quantos array a variavel possui
#  col - 1
# print(len(test[1])) #conta quantas coluna o segundo array da variavel test possui
#h = 'caixa alta'
# print(h.upper()) # deixa todos os caracteres com letras maiúsculas - CAIXA ALTA
# h1 = 'CAIXA BAIXA'
# print(h1.lower()) # deixa todos os caracteres com letras minusculas - caixa baixa

# print(h1.capitalize()) #deixa somente o primeiro caractere com letra maiuscula - Caixa baixa

# remove os espaços do da variavel
# test = h.split(' ') # transforma a variavel em array e separa elas pelo espaço ' ' - também podemos colocar caracteres
# print(test) # da para acessar cada palavra do array e só colocar a coluna que você quer acessar, por exemplo test[0] - quero acessar a primeira coluna

# print(h.replace('alta', 'alto')) # alterar uma parte da variavel por outra - cada caractere
# print(h.replace(' ', ',')) # troque o espaço pela virgula

'''
pontos = 0
print('------***Quiz***-------')
print('Vamos começa?')
inicio = input('S ou N\n')
if inicio.upper() == 'S':
    print('PRIMEIRA PERGUNTA\n')
    print('QUAL É A FUNÇÃO DO REPLACE')
    print('A) SUBSTITUIR ALGUM CARACTERE DA VARIAVEL POR OUTRO')
    print('B) TRANSFORMA A VARIAVEL EM ARRAY E SEPARADO POR ALGUM CARACTER PRESENTE NA VARIAVEL')
    print('C) VERIFICA A QUANTIDADE DE CARACTERES QUE A VARIAVEL POSSUI')
    print('D) DEIXA SOMENTE O PRIMEIRO CARACTER MAIUSCULO')
    resp = input('Digite uma da letras acima - A,B,C e D\n')
    while resp.upper() != 'A' and resp.upper() != 'B' and resp.upper() != 'C' and resp.upper() != 'D':  # enquanto não digitar uma das alternativas repita
        resp = input('Digite uma da letras acima - A,B,C e D\n')
    else:  # senão - se for digitado passe para a proxima questao
        if resp.upper() == 'A':
            pontos = pontos + 1
        print('PRIMEIRA PERGUNTA\n')
        print('QUAL É A FUNÇÃO DO SPLIT')
        print('A) SUBSTITUIR ALGUM CARACTERE DA VARIAVEL POR OUTRO')
        print('B) TRANSFORMA A VARIAVEL EM ARRAY E SEPARADO POR ALGUM CARACTER PRESENTE NA VARIAVEL')
        print('C) VERIFICA A QUANTIDADE DE CARACTERES QUE A VARIAVEL POSSUI')
        print('D) DEIXA SOMENTE O PRIMEIRO CARACTER MAIUSCULO')
        resp = input('Digite uma da letras acima - A,B,C e D\n')
        while resp.upper() != 'A' and resp.upper() != 'B' and resp.upper() != 'C' and resp.upper() != 'D':
            resp = input('Digite uma da letras acima - A,B,C e D\n')
        else:
            if resp.upper() == 'B':
                pontos = pontos + 1
            print('PRIMEIRA PERGUNTA\n')
            print('QUAL É A FUNÇÃO DO LEN')
            print('A) SUBSTITUIR ALGUM CARACTERE DA VARIAVEL POR OUTRO')
            print('B) TRANSFORMA A VARIAVEL EM ARRAY E SEPARADO POR ALGUM CARACTER PRESENTE NA VARIAVEL')
            print('C) VERIFICA A QUANTIDADE DE CARACTERES QUE A VARIAVEL POSSUI')
            print('D) DEIXA SOMENTE O PRIMEIRO CARACTER MAIUSCULO')
            resp = input('Digite uma da letras acima - A,B,C e D\n')
            while resp.upper() != 'A' and resp.upper() != 'B' and resp.upper() != 'C' and resp.upper() != 'D':
                resp = input('Digite uma da letras acima - A,B,C e D\n')
            else:
                if resp.upper() == 'C':
                    pontos = pontos + 1
                print('PRIMEIRA PERGUNTA\n')
                print('QUAL É A FUNÇÃO DO CAPTALIZE')
                print('A) SUBSTITUIR ALGUM CARACTERE DA VARIAVEL POR OUTRO')
                print('B) TRANSFORMA A VARIAVEL EM ARRAY E SEPARADO POR ALGUM CARACTER PRESENTE NA VARIAVEL')
                print('C) VERIFICA A QUANTIDADE DE CARACTERES QUE A VARIAVEL POSSUI')
                print('D) DEIXA SOMENTE O PRIMEIRO CARACTER MAIUSCULO')
                resp = input('Digite uma da letras acima - A,B,C e D\n')
                while resp.upper() != 'A' and resp.upper() != 'B' and resp.upper() != 'C' and resp.upper() != 'D':
                    resp = input('Digite uma da letras acima - A,B,C e D\n')
                else:
                    if resp.upper() == 'D':
                        pontos = pontos + 1
                    if pontos == 1:
                        print('Poxa, tem que melhorar')
                    elif pontos == 2:
                        print('Ta bom, mas podia esta melhor ')
                    elif pontos == 3:
                        print('Ta otimo, você esta indo bem')
                    elif pontos == 4:

                        print('Perfeito, Já é um DEV')
                    else:
                        print('Ai tu me quebra, nenhuma!!!')


else:
    print('Tchau :(')


# Exercicios
# Exercicio 01
#dados = input('Digite algo:\n') # entrada de dados

#veri = dados.split('.') #se ele apresenta um ponto será transformado em array

#if dados.isnumeric(): #verificando se contém somente numeros
#    primitivo = int(dados) # se for numerico, então converta para int
#elif dados == "True": # se não for  numerico e for string, porém apresenta a palavra 'True' é boleano
#    primitivo = bool(dados)
#elif dados == "False":  # se não for  numerico e for string, porém apresenta a palavra 'False' é boleano
#    primitivo = bool(dados)
#elif len(veri) > 1 and len(veri) <= 2: # se ao transformamos em array e ele tiver mais de um dados, porém menor ou igual a 2 faça
#    if veri[0].isnumeric and veri[1].isnumeric(): # verificando se em cada posição do array os dados são numericos
#        if '.' in dados: # verificando se os dados da variavel apresenta ponto
#            primitivo = float(dados) # converta para float
#else: # se não for nenhum dos casos só passa os dados da variavel 'dados' para a variavel 'primitivos'
#    primitivo = dados

#print('Tipo primitivo do dados é: {}'.format(type(primitivo))) # exiba os tipo de dados presente na variavel

#espaco = dados.isspace() # verificando se a variavel aprenseta somente espaços

#if espaco == True: # se a variavel possui somente espaços faça
#    print('Contém somente espaços:{}'.format(espaco)) # exiba o valor da variavel 'espaco' - True
#else: # se a variavel nao apresenta somente espaços
#    print('Comtém somente espaços:{}'.format(espaco)) # exiba o valor da variavel 'espaco' - False

#alfabetico = dados.isalpha() # verifica se os dados da variavel é alfabetico

#if alfabetico == True: # se for faça
#    print('É alfabetico:{}'.format(alfabetico))
#else: # senão faça
#    print('É alfabetico:{}'.format(alfabetico))

#alfanumerico = dados.isalnum() # verifica se os dados da variavel é alfanumerico

#if alfanumerico == True:
#    print('É alfanumerico:{}'.format(alfanumerico))
#else:
#    print('É alfanumerico:{}'.format(alfanumerico))

#maiusculo = dados.isupper() # verifica se os dados da variavel esta todos em maiusculo

#if maiusculo == True:
#    print('Esta em maiusculo:{}'.format(maiusculo))
#else:
#    print('Esta em maiusculo:{}'.format(maiusculo))

#minusculo = dados.islower() # verifica se os dados da variavel esta todos em minusculo

#if minusculo == True:
#    print('Esta em minusculo:{}'.format(minusculo))
#else:
#    print('Esta em minusculo:{}'.format(minusculo))

#captalize = dados.istitle() # verifica se os dados da variavel comecam com o primeiro caractere maiusculo

#if captalize == True:
#    print('Esta captalizado:{}'.format(captalize))
#else:
#    print('Esta captalizado:{}'.format(captalize))

#Exercicio 2
#Antecessor e Sucessor
#numero = input('Digite um numero\n') # entrada de dados
#while numero.isnumeric() == False: # enquanto os dados da variavel não for somente numero faça
#    numero = input('Digite um numero') # entrada de dados
#else: # se for somente numeros faça
#    ant = int(numero) - 1 # converta e subtraia
#    suc = int(numero) + 1 # converta e soma
#    print('Seu antecessor é {} e seu sucessor é {}'.format(ant, suc)) #exibir o resultado da subtração e soma