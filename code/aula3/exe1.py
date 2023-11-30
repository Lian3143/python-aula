#Condicional simples (if, only)

a = input('Insira o valor A:')
b = input('Insira o valor B:')
 
if(a>b):
     print('O número {} é maior que o número {}!' .format(a,b))

#Condicional composta (if, else)
x = int(input('Digite um valor inteiro:'))
if (x % 2 == 0):
     print('O número {} é par!' .format(x))
else:
     print('O número {} é ímpar!' .format(x))

##-----------------------------------------------------------------------
#
##Operadores lógicos 
##NOT 
#x = True
#y = False
#print(not x)
#print(not y)
##and
#x = True
#y = False
#print(x and y)
##or 
#x = True
#y = False
#
#print(x or y)

#-----------------------------------------------------------------------

#EXERCÍCIO 
media = 7
mat = float(input('Digite sua nota:'))
pt = float(input('Digite sua nota:'))
en = float(input('Digite sua nota:'))

if((mat, pt, en) <= media): 
     print('Você está aprovado!')
else:
     print('Você está reprovado!')