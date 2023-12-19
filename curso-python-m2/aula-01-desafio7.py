#Desafio 07 - Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#Equilátero: todos os lados iguais
#Isóceles: dois lados iguais
#Escaleno: todos os lados diferentes

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a + b > c and b + c > a and a + c > b:
    print(f'As retas podem formar um triângulo!')
else:
    print('As somas de dois dos lados são maiores que o terceiro lado. Portanto, não formam um triângulo.')

if a == b and b == c and a == c: #triângulo equilátero
    print(f'Como os três lados são iguais, o triângulo em questão se caracteriza como um triângulo equilátero. ')

elif a == b and b != c: #triângulo isóceles
    print(f'Por possuir apenas um lado diferente, o triângulo em questão se caracteriza como isóceles. ')
 
elif a != b and b != c and a != c: #triângulo escaleno 
    print(f'Como os três lados são diferentes, o triângulo é considerado como escaleno. ')
