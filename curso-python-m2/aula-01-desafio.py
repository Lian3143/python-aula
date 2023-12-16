#Desafio 01 - Escreva um programa para apoiar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% dos salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos planeja pagar a casa? '))

tempo_pag = anos*12 
prestacao_mes = casa/tempo_pag 
