#Desafio 05 - Escreva um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida. 
#média abaixo de 5.0 - reprovado
#média entre 5.0 e 6.9 - recuperação
#média igual ou superior a 7 - aprovado

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2)/2

if media < 5.0:
    print(f'Sua média foi de {media} e você está reprovado(a)!')

elif media >= 7:
    print(f'Sua média foi {media} e você está aprovado(a)!')

elif media >= 5 and media <= 6.9:
    print(f'Por ter conseguido a média {media} você ficou de recuperação.')

print('Encerrando programa. \nTenha um bom dia!')
