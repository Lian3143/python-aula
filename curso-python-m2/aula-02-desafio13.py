#03 - Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500. 

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

for i in range(1, 501, 2): #vai dividir a lista em apenas números ímpares. 
    if i % 3 == 0: #se o resto da divisão for igual a zero, o número é multiplo de 3. 
        print(i) #vai imprimir tudo. 

print('Aqui está todos os números ímpares entre 1 e 500 que são múltiplos de 3.')