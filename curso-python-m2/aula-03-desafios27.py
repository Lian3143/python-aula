#6 - Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

p = int(input('Primeiro termo: '))
r = int(input('Digite a razão: '))

termo = p
cont = 1 #contador para encerrar o loop
#loop para mostrar os 10 primeiros termos da progressão
while cont <= 10:   #quando o contador chegar em 10, o programa será encerrado. isso também significará que você alcançou o décimo termo.
    print(f'{termo} → ', end='')
    termo += r
    cont += 1

print('Fim.')

#loop com opções extras para o usuário.
x = 1
while x > 0:
    print(f'\nO que deseja fazer a seguir?\n 1 - Mostrar um novo termo\n 0 - Sair do programa')
    x = int(input('Qual opção deseja realizar? '))

    if x == 0: #quando a variável x receber o valor de zero, o programa irá subtrair 1 (var x equivale a 1), encerrando assim o programa.
        x -= 1
    else:
        p = int(input('Primeiro termo: '))
        r = int(input('Digite a razão: '))

        termo = p
        cont = 1

        while cont <= 10:
            print(f'{termo} → ', end='')
            termo += r
            cont += 1
    print(f'Fim. ')

print(f'Fim do programa. ')