#01 - Faça um programa que mostre na tela uma contagem regressiva para o estouro dos foguetes de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles. 
#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
from time import sleep #sleep é um contador, que adiciona um timer (definido pelo usuário) para executar o programa.

print('A contagem regressiva para os fogos vai começar!')
for i in range(10,-1,-1):
    sleep(1)
    print(i)
print('BUM!!! FELIZ ANO NOVO!!!')