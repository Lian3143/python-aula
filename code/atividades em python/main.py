#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e faça o usuário tentar advinhar qual foi o número escolhido. O programa deverá escrever na tela se o aluno acertou ou não. 

from random import randint 

print('---===JOGO DE ADIVINHAÇÃO===---')
nome = str(input('Digite o seu nome: ')).strip()
print(f'Seja muito bem-vindo ao nosso jogo, {nome}!')
