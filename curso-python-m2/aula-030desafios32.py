#2 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


cont = 0
n = 0
n2 = int(input('Digite um valor para ver sua tabuada: '))
while True:
    cont += 1
    if cont < 11:
        print(f'{n2} x {cont} = {n2 * cont}')


    if n2 < 0:
        break


print('Fim.')
