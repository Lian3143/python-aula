#Utilizando métodos/módulos com Pyton! (import / from)

#Exemplo: 
#import nome_da_biblioteca (vai importar toda a biblioteca)

#Porém, caso você não queira importar tudo isso ou queira usar apenas um recurso dessa biblioteca, pode usar o comando *from*. 
#Fica mais ou menos assim:

# from *nome_da_biblioteca* import *recurso_que_quer_importar*

#Exemplo 1

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)  #função que realiza a raiz quadrada

print(f'A raiz de {num} é igual a {raiz}.')

#Exemplo 2

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)  #função que realiza a raiz quadrada

print(f'A raiz de {num} é igual a {raiz}.')