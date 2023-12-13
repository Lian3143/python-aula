#01 - Crie um programa que leia um número Real qualquer e mostre na tela sua porção inteira
import math
n = float(input('Digite um número: '))
print(f'O número digitado foi {n} e a sua parte inteira é {math.trunc(n)}')
