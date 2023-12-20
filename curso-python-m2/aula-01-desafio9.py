#Desafio 09 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista - 10% de desconto
#à vista no cartão - 5% de desconto
#em até 2x no cartão - preço normal
#3x ou mais no cartão - 20% de juros
print('{:=^40}'.format(' Loja do Lian '))
valor = float(input(' Qual o valor que será pago pelo produto? '))
print('Qual será o método de pagamento?')

print(' 1 - À vista - 10% de desconto\n 2 - À vista no cartão - 5% de desconto\n 3 - Em até 2x no cartão - Preço normal\n 4 - 3x ou mais no cartão - 20% de juros')


pag = int(input('Qual será o método de pagamento? '))

if pag == 1: 
    calc = valor - (valor*0.10)
    print(f'  O valor do seu produto é R${valor:.2f}.\n Método de pagamento: À vista.\n Valor do desconto: 10% \n Valor final do produto com desconto: R${calc:.2f}.')

elif pag == 2: 
    calc = valor - (valor*0.05)
    print(f' O valor do seu produto é R${valor:.2f}.\n Método de pagamento: À vista no cartão.\n Valor do desconto: 5% \n Valor final do produto com desconto: R${calc:.2f}.')

elif pag == 3: 
    calc = valor/2 
    print(f' O valor do seu produto é R${valor:.2f}.\n Método de pagamento: 2x no cartão.\n Valor do desconto: Não há desconto ou acréscimo. \n Valor final do produto: R${calc:.2f}.')

elif pag == 4: 
    parcela = int(input('Você deseja parcelar em quantas vezes? '))
    calc = valor + (valor*0.20)
    final = calc / parcela
    print(f' O valor do seu produto é R${calc:.2f}.\n Método de pagamento: Parcelado em {parcela}x.\n Valor dos juros: 20% \n Valor das parcelas: R${final:.2f}.')

elif pag > 4:
    print('Método de pagamento não encontrado. Tente novamente.')