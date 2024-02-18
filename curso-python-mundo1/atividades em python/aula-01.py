#RECEBER DOIS VALORES E REALIZAR A SOMA ENTRE ELES 

v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))

soma = v1 + v2 

print(f'A soma entre {v1} e {v2} vale {soma}.')

#Desafios ---------------------------------------------

#01 - Crie um programa que leia dois números e mostre a soma entre eles
v1 = int(input('Digite o primeiro valor'))
v2 = int(input('Digite o segundo valor'))

soma = v1 + v2

print(f'A soma entre {v1} e {v2} é igual a {soma}')


#02 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela. 

a = input('Digite qualquer coisa:')

print(type(a))

print('é numério?', a.isnumeric())
print('é espaço?', a.isspace())
print('é alpabético?', a.isalpha())
print('É tudo maiúsculo?', a.isupper())
print('É tudo minúsculo?', a.islower())
print('Está capitalizado?', a.istitle())

print('É tudo alfanumérico?', a.alphanum())