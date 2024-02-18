#07 - Faça um progrma que leia um número inteiro e diga se ele é ou não um número primo.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
n = int(input('Digite um número: '))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m',end=' ')
    print(f'{i}', end=' ')

print(f'\n\033[mO número {n} foi dividio {cont} vezes.')

if cont == 2:
    print(f'Portanto, é um número primo.')
else:
    print(f'Portanto, não é um número primo.')