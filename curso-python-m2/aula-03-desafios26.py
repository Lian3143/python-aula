#5 - Refaça o DESAFIO51, lendo o primeiro termo e a razãp de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

#UTILIZANDO O FOR
p = int(input('Primeiro termo: ')) #primeiro termo
r = int(input('Razão: ')) #razão
d = p + (10 - 1) * r  #decimo termo

for i in range(p, d + r, r):
    print(f'{i}', end=' ')
    print(' =>', end=' ')

print('Acabou. \nEncerrando programa... ')



#RESOLUÇÃO UTILIZANDO O WHILE
p = int(input('Primeiro termo: '))
r = int(input('Digite a razão: '))

termo = p
cont = 1

while cont <= 10:
    print(f'{termo} → ', end=' ')
    termo += r
    cont += 1
print(f'Fim.')