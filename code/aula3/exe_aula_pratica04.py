print('Seja bem vindo à minha loja!')
valor_produto = float(input('Digite o valor do produto:'))
qnt_produto = float(input('Digite a quantidade desejada:'))
desconto_produto = 0

if (qnt_produto <=4):
    desconto_produto = 0
elif (qnt_produto >= 5) and (qnt_produto <= 19):
    desconto_produto = 0.03
elif (qnt_produto >= 20) and (qnt_produto <= 99):
    desconto_produto = 0.06
else:
    desconto_produto = 0.10

total_sem_desconto = valor_produto + qnt_produto
print(f'O valor do produto SEM desconto é: {total_sem_desconto}.')
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print(f'O valor do produto COM desconto é: {total_com_desconto}.')