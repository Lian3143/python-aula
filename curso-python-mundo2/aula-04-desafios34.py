#4 - Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados
#C) quantas mulheres tem menos de 20 anos.

#variável de apoio
mais_dezoito = 0
mulheres_menos_vinte = 0
homens_cadastrados = 0
cont = 0

print(f'Olá, seja bem-vindo!')
#loop
while True:
    idade = int(input('Informe a sua idade: '))
    sexo = str(input(f'Informe o seu sexo [M/F]: ')).strip().lower()
    cont += 1
    #estruturas de controle
    continuar = str(input('Deseja continuar?\nDigite "S" para continuar ou "N" para sair: ')).strip().lower()
    if continuar == 's':
        if idade > 18:
            mais_dezoito += 1

        if sexo == 'm':
            homens_cadastrados += 1

        if sexo == 'f' and idade <= 20:
            mulheres_menos_vinte += 1
    elif continuar == 'n':
        break
    elif continuar != 's' or continuar != 'n':
        print('Comando inválido. Tente novamente.')


#print com o resultado requerido
print(f'Foram cadastrados {cont} pessoas.')
print(f'{homens_cadastrados} homens.\nAlém de {mais_dezoito} pessoas maiores de dezoito anos.\nUm total de {mulheres_menos_vinte} mulheres possuem menos de 20 anos. ')



