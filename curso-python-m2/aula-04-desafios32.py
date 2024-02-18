#2 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n1 = 0

while True:
    #recebendo um valor
    n1 = int(input('Digite um valor para ver sua tabuada: '))

    if n1 < 0: #encerrando o programa caso o "flag" seja digitado.
        print(f'Finalizando programa...')
        break
    #imprimindo a tabuada
    else:
        for i in range(1,11):
            print(f'  {n1} x { i } = {n1*i}')

#print final
print('Programa finalizado.')
