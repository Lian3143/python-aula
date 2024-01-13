#4 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120

#resolvendo utilizando uma biblioteca
'''from math import factorial
x = int(input('Digite um valor para descobrir o seu fatorial: '))
f = factorial(x)
print(f'{x}! é igual a: {f}')'''

#resolvendo sem biblioteca

x = int(input('Digite um valor para descobrir o seu fatorial: '))

c = x
f = 1

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' =', end='')
    f *= c
    c -= 1

print(f)