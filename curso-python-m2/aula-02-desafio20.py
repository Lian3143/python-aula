#10 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
#Quantidade de pessoas
pessoas = 5
#Var de apoio
maior_peso = 0
menor_peso = 0

for i in range(1, pessoas+1):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))

#verificando o maior e o menor peso
    if peso > peso:
        maior_peso += peso
    elif peso < peso: 
        menor_peso +- peso

#print com o resultado
print('-=-'*20)
print(f'O maior peso é: {maior_peso}\nO menor peso é: {menor_peso}')
print('-=-'*20)
