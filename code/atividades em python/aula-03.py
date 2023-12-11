#Utilizando métodos/módulos com Pyton! (import / from)

#Exemplo: 
#import nome_da_biblioteca (vai importar toda a biblioteca)

#Porém, caso você não queira importar tudo isso ou queira usar apenas um recurso dessa biblioteca, pode usar o comando *from*. 
#Fica mais ou menos assim:

# from *nome_da_biblioteca* import *recurso_que_quer_importar*

#Exemplo 1

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)  #função que realiza a raiz quadrada

print(f'A raiz de {num} é igual a {raiz}.')

#Exemplo 2

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)  #função que realiza a raiz quadrada

#exemplo 3 

print(f'A raiz de {num} é igual a {raiz}.') 


import random #Biblioteca RANDOM gera números aleatórios. random.randint gerará um número inteiro de 1 à 10. Enquanto random.random gerará um número float de 0 à 1. 
num = random.randint(1,100)
print(num)

#ATIVIDADES/DESAFIOS

#01 - Crie um programa que leia um número Real qualquer e mostre na tela sua porção inteira

#02 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimeto da hipotenusa 

#03 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

#04 - Um professor quer sortear um dos seus quatro
