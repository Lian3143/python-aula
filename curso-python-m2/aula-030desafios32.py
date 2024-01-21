#2 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


cont = 0
n = 0
n2 = int(input('Digite um valor para ver sua tabuada: '))
while True:
    if n2 < 0:
        break
    else:
        if cont <= 10:
            print(f'{n2} x {cont} = {n2 * cont}')
            cont += 1
        n2 = int(input('Digite um valor para ver sua tabuada: '))



print('Fim do programa.')
