#CONDIÇÕES SIMPLES E ANINHADAS 
#IF E ELSE

#exemplo
condicao = ''
if condicao.esquerda():
    print(f'condicao')

else: 
    print(f"condicao")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#AULA PRÁTICA! 

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2

if m >= 6.0:
    print('Sua nota está boa! Parabéns')
else:
    print("Sua nota está ruim! Estude mais")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#ATIVIDADES | DESAFIOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#01 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e faça o usuário tentar advinhar qual foi o número escolhido. O programa deverá escrever na tela se o aluno acertou ou não. 

from random import randint

random = randint(0,5)

a = int(input('Qual número eu pensei? '))
if a == random: 
    print("Você acertou! Parabéns!")
else: 
    print('Você errou! Tente novamente!')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#02 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado. A multa vai custar R$7.00 reais por cada KM acima do limite. 

km = int(input('Qual a velocidade do carro em KM? '))

if km >= 80:
    print(f'Você está acima do limite de velocidade e será multado! O valor da multa será R${km*7} reais. ')
else:
    print(f'Sua velocidade está no limite permitido. Prossiga.')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#03 - Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar. 

n = int(input('Digite um número inteiro qualquer: '))
if n % 2 == 0: #o sinal de '%' vai dividir 'n' por '2' e irá pegar o resto da divisão e comparar com 0, se o resultador for True vai imprimir a primeira linha, caso contrario a segunda. 
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é ímpar!')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#04 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.

km = int(input('Digite quantos KM serão percorridos na viagem: '))

if km <= 200: #vai comparar se km é igual ou menor a 200. 
    print(f'Ao percorrer {km}KM, você terá que pagar {km*0.50:.2f} na passagem.')
else:
    print(f'Ao percorrer {km}KM, você terá que pagar {km*0.45:.2f} na sua passagem.')

print('Boa viagem!')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#05 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#06 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#07 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%. 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#08 - Desenvolva um programa que leia o comprimento de três rotas e diga ao usuário se elas podem ou não formar um triângulo.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
