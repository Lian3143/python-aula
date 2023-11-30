#TUPLAS
escolha = ('1. Adição', '2. Subtração ', '3. Multiplicação', '4. Divisão', '5. Sair')
print('Qual operação deserja realizar?')
for item in escolha:
    print(f'{item}')


#JUNÇÃO DE TUPLAS
#EX 

mochila_normal = ('Sabonete', 'camisa', 'banana') 
upgrade = ('Bacon', 'canivete')

mochila_grande = mochila_normal + upgrade 

print(mochila_grande) #A IMPRESSÃO VAI JUNTAR AS DUAS VÁRIAVEIS EM UMA SÓ, ACRESCENTANDO OS ITENS DE UMA NA OUTRA. PRESTAR ATENÇÃO NA ORDEM, POIS ISSO AFETA O RESULTADO FINAL


#