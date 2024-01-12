#10 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

#Var de apoio

maior_peso = 0
menor_peso = 0

for i in range(1, pessoas+1):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))

#verificando o maior e o menor peso
if i == 1:
    maior_peso = peso
    menor_peso = peso
    
    
#print com o resultado

print(f'O maior peso é: {maior_peso}\nO menor peso é: {menor_peso}')

