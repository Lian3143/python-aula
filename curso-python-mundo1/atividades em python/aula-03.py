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
num = random.randint(1,100) #random.randint serve para gerar números aleatórios. basta especificar dentro do parênteses onde você quer que ele comece e onde quer que termine. 
print(num)

#ATIVIDADES/DESAFIOS

#01 - Crie um programa que leia um número Real qualquer e mostre na tela sua porção inteira
import math
n = float(input('Digite um número: '))
print(f'O número digitado foi {n} e a sua parte inteira é {math.trunc(n)}')


#02 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimeto da hipotenusa 

import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

calc = math.hypot(oposto, adjacente)

#segunda maneira de resolver esse calc 

import math 

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

calc = (oposto**2) + (adjacente**2) #o calculo da hiputenusa é: x**2 = a**2 + b**2

print(f'Se a o cateto oposto é {oposto} e o cateto adjacente é {adjacente}, a hipotenusa será {math.sqrt(calc):.2f}. ') #math.sqrt realiza a raiz quadrada 

#03 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
import math

a = float(input("Digite um ângulo: "))

#OBS: Primeiro será necessário transformar em radiano, e para isso você pode utilizar o parâmetro math.radians(). 
cos = math.cos(math.radians(a)) #Retorna cosseno de x.
seno = math.sin(math.radians(a)) #Retorna o seno de x.
tan = math.tan(math.radians(a)) #Retorna o tangente de x.
print(f'O seno é {seno:.2f}, o cosseno é {cos:.2f} e a tangente é {tan:.2f}.')

#04 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
print(f'O aluno escolhido para apagar o quadro foi: {choice([aluno1, aluno2, aluno3, aluno4])}') #choice irá escolher um nome dentro da lista e irá mostar ele na tela
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#OUTRA MANEIRA DE RESOLVER A QUESTÃO
from random import choice 
alunos = str(input('Digite o nome dos quatro alunos, separados por espaço e vírgula: ')).strip()
replace = alunos.replace(',', ' ')
lista = replace.split()
print(f'O aluno escolhido para apagar o quadro foi: {choice(lista)}.')
#05 - O mesmo professor do desafio anterior que sortear a ordem de apresenação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 
from random import shuffle 

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4] #transforma o nome dos alunos em uma lista
shuffle(lista)  #o comando 'SHUFFLE irá embaralhar a lista

print(f'A lista ordem sorteada foi: {lista}') #fará o print de tudo

#06 - Faça um programa em python que abra e reproduza o áudio MP3. 

import pygame

pygame.init()
pygame.mixer.music.load('ex03.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#OBS: NÃO CONSEGUI FAZER FUNCIONAR NO VISUAL, APENAS NO PYCHARM




#ATIVIDADE EXTRA UTILIZANDO BIBLIOTECAS! AQUI UTILIZAREI A BIBLIOTECA TKINTER PARA GERAR INTERFACES GRÁFICAS
import requests
from tkinter import * #é mais vantajoso importar a biblioteca desta forma

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto #definirá o texto que aparecerá após clicar no botão. 




janela = Tk() #definirá a criação da janela
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

janela.title('Cotação atual das moedas') #O comando TITLE serve para alterar o titulo da janela
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
janela.geometry('300x200') #vai definir o tamanho da janela
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


texto_de_orientação = Label(janela, text =' Clique no botão abaixo para exibir as cotações') #label serve para exibir textos. Primeiro você deverá especificar em qual janela ele fará parte e, após isso, colocara o comando TEXT = 'Digite o seu texto aqui '. 

texto_de_orientação.grid(column = 0, row=0, padx=20, pady=20) #column = coluna / row = linha. Esse comando .grid especificará onde vai ficar o texto na tela. você deve especificar a coluna e a linha. padx e pady significam padding.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

botao = Button(janela, text = 'Clique aqui para exibir as cotações ', command=pegar_cotacoes) #Isso adicionará um botão na tela. Primeiro, você vai dizer em que janela o botão deve ficar. Depois, vai dizer o texto que vai conter no botão e, logo após, irá definir um comando(função) para esse botão.

botao.grid(column=0, row=1) #isso mostrará onde o botão aparecerá, assim como o texto. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

texto_cotacoes = Label(janela, text=' ')
texto_cotacoes.grid(column=0, row=2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


janela.mainloop() #essa é sempre a última linha de código de um código, pois ele é quem fará com que a janela fique sempre em exibição, sem fechar automaticamente. 

