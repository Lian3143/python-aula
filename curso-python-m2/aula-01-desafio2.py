#Desafio 02 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

num = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão para este número? ')
bi = print('1 - Binário')
oc =   print('2 - Octal')
he =    print('3 - Hexadecimal')
escolha = int(input('Para qual das três opções você deseja converter? '))

if escolha == 1:
    binario = bin(num)
    print(f'O número {num} convertido para binário é {binario}.')

elif escolha == 2:
    octal = oct(num)
    print(f'O número {num} convertido para octal é {octal}.')

elif escolha == 3:
    hexadecimal = hex(num)
    print(f'O número {num} convertido para hexadecimal é {hexadecimal}.')

else:
    print('Este número não corresponde à uma das opções. ')
print('Programa encerrado. ')


