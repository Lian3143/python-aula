#05 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitador for ímpar, desconsidere-o.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
x = 0
c = 0
for i in range(1,7):
    a = int(input(f'Digite {i}° valor: ')) #vai receber varios valores
    if a % 2 == 0: #vai definir se os valores recebidos são par ou impar
        c += 1
        x += a #os numeros pares serão somados aqui

print(f'O resultado da soma de todos os {c} números pares é: {x}.\nEncerrando programa... ')