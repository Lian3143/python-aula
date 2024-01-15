#7 - Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma sequência fibonacci.

x = int(input('Quantos termos você quer ver dentro da sequência fibonacci: '))


cont = 1 #contador
a = 0 #primeiro termo fixo
b = 1 #segundo termo fixo
c = 0 #terceiro termo, que será a soma do primeiro com o segundo termo
print(f'{a} → {b} → ', end='')
#estrutura de repetição
while cont < x+1:
    c = a + b
    print(f'{c} → ', end='')
    #para realizar a soma, o programa fará o primeiro termo receber o valor do segundo, e o segundo o do terceiro, somando-os entre si e alterando o seu valor até o contador chegar ao seu final.
    a = b
    b = c
    #contador receberá o seu valor (1) e somará 1 toda vez que o loop for repetido.
    cont += 1

print(f'Fim. ')