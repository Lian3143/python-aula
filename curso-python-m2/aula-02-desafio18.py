#08 - Crie um programa que leia uma frase qualquer e diga se é um políndromo, desconsiderando os espaços. 
#Exemplo: Após a sopa, de trás pra frente e desconsiderando os espaços.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

frase = str(input('Digite um políndromo: ')).strip().upper()

x = 0
for i in range(1, 10):
    print(frase)
print(i)    