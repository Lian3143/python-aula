#1 - crie um programa que leia vários números inteiros pelo teclado.
# O programa só será interrompido quando o usuário digitar o valor "999", que é  a condição de parada.
# No final, mostre qunatos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag).

#-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=
#variável de apoio
n = 0
cont = 0
soma = 0
flag = 999
#loop infinito

while True:
    n = int(input('Digite um valor (para sair digite "999"): '))

    #definindo o "flag" para parada do loop.
    if n == flag:
        print(f'Finalizando programa.')
        break
    soma += n #somando os valores entre si.
    cont += 1 #contador.

#print com o resultado.
print(f'Foram digitados {cont} números e a soma entre eles é: {soma}.')