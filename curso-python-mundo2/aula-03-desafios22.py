#1 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ' '

while sexo == "M" or "F":
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip() #solicitando o sexo via input

    if sexo != 'M' and sexo != 'F': #verificando se é igual a 'M' ou 'F'
        print(f'O sexo digitado não foi identificado. Por favor, tente novamente. ')
    else:
        print('Dado cadastrado. ')

print('Encerrando programa...')

