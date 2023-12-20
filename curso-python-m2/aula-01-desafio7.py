#Desafio 07 - Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#Equilátero: todos os lados iguais
#Isóceles: dois lados iguais
#Escaleno: todos os lados diferentes



a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a + b > c and b + c > a and a + c > b: #vai verificar se as retas podem formar um triângulo. 
    print(f'As retas podem formar um triângulo ', end='')
    if a == b == c: #vai verificar se os três lados são iguais. 
        print(f'equilátero.')
    elif a != b != c != a: #vai verificar se os três lados são diferentes.  (OBS: você tem que verificar se "c" é diferente de "a".)
        print(f'escaleno.')
    else: #se não for equilátero e nem escaleno, será isóceles. 
        print('isóceles.')
else:
    print('As somas de dois dos lados são maiores que o terceiro lado e, portanto, não formam um triângulo.')