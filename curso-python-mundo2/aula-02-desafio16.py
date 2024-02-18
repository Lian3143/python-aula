#06 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

p = int(input('Primeiro termo: ')) #primeiro termo
r = int(input('Razão: ')) #razão
d = p + (10 - 1) * r  #decimo termo

for i in range(p, d + r, r):
    print(f'{i}', end=' ')
    print(' =>', end=' ')

print('Acabou. \nEncerrando programa... ')