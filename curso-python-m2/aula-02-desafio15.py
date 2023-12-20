#05 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitador for ímpar, desconsidere-o.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
x = 0
for i in range(1,7):
    a = int(input('Digite um valor: ')) #vai receber varios valores
    if a % 2 == 0: #vai definir se os valores recebidos são par ou impar
        x += a #os numeros pares serão somados aqui
    else:
        print('Valor inválido. São permitidos apenas números pares. ') #os valores ímpares serão apenas desconsiderados aqui embaixo 
print(f'O resultado da soma de todos os números pares é: {x}.\nEncerrando programa... ')