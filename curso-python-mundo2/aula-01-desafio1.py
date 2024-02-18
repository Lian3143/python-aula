#Desafio 01 - Escreva um programa para apoiar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% dos salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos planeja pagar a casa? '))

prestacao = casa / (anos*12) 
porcentagem = salario * 0.30

print(f'Para pagar uma casa de R${casa:.2f}, você terá que pagar um total de R${prestacao:.2f} por mês.')
if prestacao <= porcentagem:
    print(f'Emprestimo aprovado! ')

else:
   print(f'Emprestimo negado. O valor da prestação supera 30% do seu pagamento e, por isso, seu emprestimo será negado. ')



#RESPOSTA DO PROFESSOR GUSTAVO 
   
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos planeja pagar a casa? '))

prestacao = casa / (anos*12)  #vai descobrir o valor das pretações mensais da casa
minimo = salario * 0.30 #vai pegar o valor minimo que ele pode pagar (30% do salario)

print(f'Para pagar uma casa de R${casa:.2f}, você terá que pagar um total de R${prestacao:.2f} por mês.')
if prestacao <= minimo:
    print(f'Emprestimo aprovado! ')

else:
   print(f'Emprestimo negado. O valor da prestação supera 30% do seu pagamento e, por isso, seu emprestimo será negado. ')