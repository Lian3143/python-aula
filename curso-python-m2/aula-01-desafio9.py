#Desafio 09 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista - 10% de desconto
#à vista no cartão - 5% de desconto
#em até 2x no cartão - preço normal
#3x ou mais no cartão - 20% de juros

valor = float(input('Qual o valor que será pago pelo produto? '))
print('Qual será o método de pagamento?')

print('1 - À vista - 10% de desconto')
print('2 - À vista no cartão - 5% de desconto')
print('3 - Em até 2x no cartão - Preço normal')
print('4 - 3x ou mais no cartão - 20% de juros')

pag = int(input('Qual será o método de pagamento? '))

if pag == 1: 
    calc = valor - (valor*0.10)
    print(f'O valor do seu produto é R${valor:.2f}.\nMétodo de pagamento: À vista.\nValor do desconto: 10% \nValor final do produto com desconto: R${calc:.2f}.')

elif pag == 2: 
    calc = valor - (valor*0.05)
    print(f'O valor do seu produto é R${valor:.2f}.\nMétodo de pagamento: À vista no cartão.\nValor do desconto: 5% \nValor final do produto com desconto: R${calc:.2f}.')

elif pag == 3: 
    calc = valor 
    print(f'O valor do seu produto é R${valor:.2f}.\nMétodo de pagamento: 2x no cartão.\nValor do desconto: Não há desconto. \nValor final do produto: R${calc:.2f}.')

elif pag == 4: 
    calc = valor + (valor*0.20)
    print(f'O valor do seu produto é R${valor:.2f}.\nMétodo de pagamento: À vista.\nValor dos juros: 10% \nValor final do produto com juros: R${calc:.2f}.')

elif pag > 4:
    print('Método de pagamento não encontrado. Tente novamente.')