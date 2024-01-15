#9 - Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar se o usuário quer ou não continuar a digitar os valores.


#variáveis de apoio
maior = 1
menor = 1
media = 0
cont = 1
a = 1
x = 0

#estrutura de repetição

while a != 0:
    x = int(input('Digite um inteiro: '))
    cont += 1

    #estrutura condicional para definir o maior e o menor valor
    if cont == 1:
        maior = x
        menor = x
    if x > maior:
        maior = x
    elif x <= menor:
        menor = x

    #opções para continuar ou encerrar o programa
    print('-=-' * 20)
    print('Deseja continuar a execução do programa?\n 1 - Continuar\n 0 - Sair do programa ')
    a = int(input('Qual opção deseja realizar? '))
    print('-=-' * 20)
    if a == 0:
        a - 10
    elif a > 1:
        print(f'Valor inválido. Digite novamente.')
    media += x

#print com o resultado
print(f'A média entre os valores é: {media / cont-1:.2f}\nO maior digitado valor foi {maior} e o menor valor digitado é {menor}.')


print(f'Fim do programa.')