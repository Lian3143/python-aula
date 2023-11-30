total_pessoas = 0
dinheiro = 0

while True:
    idade_cliente = input('Informe a sua idade:')
    if (idade_cliente == 'sair'):
        break
    idade_cliente = int(idade_cliente)
    total_pessoas += 1
    if (idade_cliente < 3):
        ingresso = 0
    else: 
        if (idade_cliente > 12):
            ingresso = 30
        else:
            ingresso = 15
    dinheiro =+ ingresso 

media = total_pessoas / dinheiro

print(f'Total de pessoas: {total_pessoas}')
print(f'Total arrecadado: {dinheiro}')
print(f'Média arrecadada: {media}')




