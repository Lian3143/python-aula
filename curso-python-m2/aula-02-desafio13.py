#03 - Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500. 

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
somatorio = 0
contador = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        contador += 1 #isso é um contador. Ele vai receber ele mesmo (zero) + a quantidade de vezes que o programa foi executado (ele + 1). 
        somatorio += i #isso é chamado de acumulador. Ele vai receber o valor que ele já tem (zero)  e vai adicionar mais o valor da variável de apoio (i). 

print(f'A soma de todos os {contador} valores é {somatorio}')