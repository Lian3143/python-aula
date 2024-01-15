#8 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsiderando o flog.)

cont = 0
soma = 0
x = 0

#loop
while x != 999:

    x = int(input('Digite um valor: '))
    cont += 1 #toda vez que o loop for realizado o contador receberá +1
    soma += x #vai somar os valores digitados e armazenar na variável "soma"

print(f'Foram digitados {cont-1} números.\nSoma dos números digitados é igual a {soma-999}')

