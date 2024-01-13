#3 - Crie um programa que leia dois valores e mostre um menu na tela:
#1 - soma
#2 - multiplicar
#3 - maior
#4 - novos números
#5 - ecerrar programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
#introdução ao programa
print('Olá, seja bem-vindo! Abaixo seguirá uma lista com as opções para o nosso programa. Fique à vontade!')

#variável de apoio
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
x = 0
#laço de repetição
while x != 5:
    sleep(1)
    print('-==-'*10)
    print('Qual operação deseja realizar?\n1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Ler novos valores\n5 - Encerrar programa') #opções do programa
    print('-==-' * 10)
    x = int(input('-> Digite a opção desejada (1-5): '))


    #verificando a opção escolhida pelo usuário
    if x == 1:
        soma = a + b
        print('-==-' * 10)
        print(f'A soma entre {a} e {b} é: {soma}')


    elif x == 2:
        multiplicacao = a * b
        print('-==-'*10)
        print(f'O resultado da multiplicação entre {a} e {b} é {multiplicacao} ')


    elif x == 3:
        if a > b:
            print(f'O maior valor entre {a} e {b} é {a}. ')
        else:
            print(f'O maior valor entre {a} e {b} é {b}. ')

    elif x == 4:
        a = int(input('Digite o novo valor: '))
        b = int(input('Digite o novo valor: '))

    elif x > 5: #delimitando um limite para o programa (para que não possa ser digitado um valor fora das opções.
        print(f'O valor informado não corresponde às opções disponíveis. Por favor, tente novamente digitando um valor válido.')

print(f'Estamos encerrando o nosso programa. Obrigado por utilizar! Volte sempre!\nFinalizando programa...')







