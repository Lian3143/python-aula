#Desafio 06 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#até 9 anos - Mirim
#até 14 anos - infantil
#até 19 anos - sênior
#acima - master

from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento: '))

data = date.today() 
ano = int(f'{data.year}') 
idade = ano - ano_nascimento #aqui eu vou descobrir a idade da pessoa

if idade < 9:
    print(f'Por ter {idade} anos você ficou na categoria mirim. ')

elif idade > 9 and idade < 14:
    print(f'Por ter {idade} anos você ficou na categoria infantil.')

elif idade > 14 and idade < 19:
    print(f'Por ter {idade} anos você ficou na categoria sênio. ')

elif idade >= 19:
    print(f'Por ter {idade} você ficou na categoria master. ')

print(f'Obrigado pela preferência! \nEncerrando programa...')