#Estruturas de repetições e iterações (FOR E WHILE)

#laço de variável de controle é chamado de for

#em PT-BR laço "c" no intervalo de (1, 10) (identação é importante, igual o if, else e elif)


#na linguagem python, fica assim:

for c in range(1,10): #fica exatamente como em ingles
    print('boa noite') #comandos que serão executados 

#comandos fora do ciclo de repetição

#EXEMPLOS ----- AULA PRÁTICA

#Imprimindo "OI" 6x seguidas. 

for i in range(1,6): #para i(var) em intervalo de (1,6). O primeiro número antes da virgula delimita onde começa, e o segundo numero dps da virgula onde termina. 
    print('Olá, mundo!') #Ele sempre vai contar um a menos do numero que vc colocou. Ex: se colocar 6, vai até o 5. Se colocar 5, vai até o 4. 

print('FIM DO PROGRAMA') #esse comando será executado após o laço ser executado

#outros exemplos

for i in range(6, 0, -1): #vai contar de 1 - 6, só que ao contrário. o terceiro número após a virgula é o iteirador, ou seja, vai definir o que vai acontecer com os outros dois. 
    print(i)              #se vai pular de 2 em 2, se vai contar ao contrário e etc. 

#mais um exemplo 

n = int(input('Digite um número: ')) #essa estrutura vai fazer com que você delimite um contador utilizando uma variável com input. 

for i in range(0, n+1):
    print(i)

print("FIM")

#mais exemplos

a = 0

for i in range(0,3):
    b = int(input('Digite um número: '))
    a = a + b #pode se fazer assim a+=b, que dá na mesma coisa. 

print(f'O somatório de todos os valores é igual a {a}. ') #esse comando vai realizar a somatória de todos os números que serão recebidos na variável b

