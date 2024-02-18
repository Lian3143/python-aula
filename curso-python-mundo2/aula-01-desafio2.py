#Desafio 02 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

num = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão para este número? \n1 - Binário\n2 - Octal\n3 - Hexadecimal ')

escolha = int(input('Para qual das três opções você deseja converter? '))

if escolha == 1:
    binario = bin(num) #bin vai converter um número para binário
    print(f'O número {num} convertido para binário é {binario}.')

elif escolha == 2:
    octal = oct(num) #oct vai converter um número para octal
    print(f'O número {num} convertido para octal é {octal}.')

elif escolha == 3:
    hexadecimal = hex(num) #hex vai converter um número para hexadecimal 
    print(f'O número {num} convertido para hexadecimal é {hexadecimal}.')

else:
    print('Este número não corresponde à uma das opções. ')
print('Programa encerrado. ')


