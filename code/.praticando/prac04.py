#receber valor
nome_cliente = input('Digite o seu nome:')
idade_cliente = int(input('Digite a sua idade:'))

if idade_cliente >= 18: #comparador de idade
    print(f'Olá, {nome_cliente}. Seja bem-vindo à nossa loja!')
    print(f'Escolha o que vai querer de acordo com a lista à seguir:')
    print('1 - Maçã')  # 2.30
    print('2 - Banana')  # 1.85
    print('3 - Laranja')  #2.20
    print('4 - Abacate')  # 3.00
    print('5 - Mamão')  # 4.00
    produto = int(input('O que vai querer?'))
    qnt_produto = int(input('Quantos você vai querer?'))

    if (qnt_produto >= 1) and (qnt_produto <= 10): 
        desconto_produto = 0.00
    elif (qnt_produto >= 11) and (qnt_produto <= 20):
        desconto_produto = 0.06
    elif (qnt_produto >= 21) and (qnt_produto <= 50):
        desconto_produto = 0.10
    elif (qnt_produto >= 50) and (qnt_produto <= 100):
        desconto_produto = 0.15
    else: 
        desconto_produto = 0.15
else:
    print('Para ter acesso ao nosso site é necessário se maior de idade.')
    print('Finalizando programa...')

if (produto == 1):
    valor_sem_desconto = qnt_produto*2.30
    valor_com_desconto = valor_sem_desconto - (valor_sem_desconto*desconto_produto)
elif (produto == 2):
    valor_sem_desconto = qnt_produto*1.85
    valor_com_desconto = valor_sem_desconto - (valor_sem_desconto*desconto_produto)
elif (produto == 3):
    valor_sem_desconto = qnt_produto*2.20
    valor_com_desconto = valor_sem_desconto - (valor_sem_desconto*desconto_produto)
elif (produto == 4):
    valor_sem_desconto = qnt_produto*3.00
    valor_com_desconto = valor_sem_desconto - (valor_sem_desconto*desconto_produto)
elif (produto == 5):
    valor_sem_desconto = qnt_produto*4.00
    valor_com_desconto = valor_sem_desconto - (valor_sem_desconto*desconto_produto)
print(f'O valor da sua compra é {valor_com_desconto}.')
