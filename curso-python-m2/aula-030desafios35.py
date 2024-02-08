#5 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:

#a) qual o total gasto na compra
#b) quantos produtos custam mais de R$ 1000. ☺
#c) qual é o nome do produto mais barato.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

#variável de apoio
mais_de_mil = 0
nome_barato = ''
produto_mais_barato = 0
total_gasto = 0
cont = 0
#loop
while True:
    #variaveis
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()
    cont += 1
    #condicionais
    if continuar == 'n':
        print('Obrigado por utilziar o nosso programa! ☻\nAqui está o resultado dos dados coletados: ')
        break
    elif continuar == 's':
        #produtos que custam mais de mil
        if preco >= 1000:
            mais_de_mil += 1

        #produto mais barato

        produto_mais_barato = preco
        nome_barato = produto

        #verificando mais barato com estrutura de controle
        if produto <= preco:
            produto_mais_barato = preco
            nome_barato = produto

#print final com o resultado requerido
print(f' O total gasto na compra foi {total_gasto:.2f}.\n O nome do produto mais barato é:{nome_barato} e ele custa {produto_mais_barato}.\n', end='')
if mais_de_mil == 1:
    print(f' Apenas um produto custa mais de mil reais.', end='')
else:
    print(f' {mais_de_mil} produtos custam mais de mil reais.', end='')