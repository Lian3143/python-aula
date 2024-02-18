#Operadores aritméticos         |  #Ordem de precedência dos operadores lógicos

# + = adição                    |   1 = ()
# - = subtração                 |   2 = ** (divisão inteira)
# * = multiplicação             |   3 = *, /, //, %          
# / = divisão                   |   4 = +, -
# // = divisão inteira          |     
# % = resto de divisão          | 

#------------------------------------------------------------------------------

#EXEMPLOS

v1 = int(input('Digite um valor'))
v2 = int(input('Digite um  segundo valor'))

a = v1 + v2
s = v1 - v2
d = v1 / v2
m = v1 * v2 
di = v1 // v2
e = v1 ** v2

print(f'A adição dos dos dois números escolhidos é {a}, a subtração é {s} a divisão é {d} e a multiplicação é {m}.', end=' ')
print(f'A divisão inteira é {di} e a exponenciação é {e}.')


#DESAFIOS ------------------------------------------------------------------------------

#01 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
n = int(input('Digite um número: '))

print(f'Analisando o númerp {n}, podemos dizer que seu antecessor é {n-1} e seu sucessor é {n+1}.')

#02 - Faça um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 
n = int(input('Digite um número: '))
print(f'O dobro de {n} é: {n*2}.\n O seu triplo é: {n*3}.\n E a sua raiz quadrada é: {n*(1/2)}.')

#03 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. 
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua seugnda nota: '))

print(f'A sua média é { (n1 + n2)/2}!')

#04 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros
n = float(input('Digite o valor em metros: '))

print(f' {n} metros convertidos para centímetros é igual a {n*100}.\n Já em milímetros é igual a {n*1000} milímetros.')
#05 - Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada
num = int(input('Digite um número: '))
v = 0

print(f'Tabuada do {num}.')

while (v <= 10):
    print('{} x {} = {}' .format(v, num, v*num))
    v = v + 1 
#06 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. (Considere 1 dólar = 3,27)
qnt = float(input('Quantos reais você têm?'))
calc = qnt/3.27

print('Se você possui {} reais, então você poderá comprar {:.2f} dólares.' .format(qnt, calc ))

#07 - Faça um programa que leia a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m**2 

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print(f'A sua parede tem a dimensão de {larg}x{alt}, e uma área de {area}.\nPara pintar essa parede, você precisará de {area/2} litros de tinta.')

#08 - Faça um algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto.
preco = float(input('Digite o valor do produto: '))
desconto = int(input('Digite o valor do desconto aplicado: '))

calc = preco * (desconto/100)
valor = preco - calc

print(f'O valor do produto é {preco} e o desconto aplicado será {desconto}.\n O valor do produto com desconto é: {valor}.')

#09 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário: '))
aumento = salario * 0.05

print(f'O seu salário atual é {salario}.\nCom o aumento de 5%, ficará {aumento}.')

#10 - Escreva um programa que converta  uma temperatura digitada em °C e converta para °F1
c = float(input('Qual a temperatura em °C? '))

conv = ( ( 9 * c) / 5 ) + 32
print (f'Se a sua temperatura é de {c:.2f} graus °C, em °F ela será igual a {conv}. ')

#11 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, e a quantidade de dias pelo qual ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 reais por dia e R$0.15 por km rodado.

km = float(input('Quantos KMs foram percorrigos pelo carro? '))  
dias = int(input('Por quantos dias ele foi alugado? '))

calc = (dias * 60) + (km * 0.15)
print(f'Após {dias} dia de aluguel e {km}km percorridos, você terá que pagar um total de {calc}')