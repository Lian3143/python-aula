#Desafio 03 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior.
# o segundo valor é maior. 
# os dois valores são iguais

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 == v2: 
    print('Os dois valores são iguais.')

elif v1 > v2:
    print(f'O maior valor é: {v1}.\nO segundo maior: {v2}.')

else:
     print(f'O maior valor é: {v2}.\nO segundo maior: {v1}.')