#Cadeias de caractéres e manipulação de texto (string).
#Sempre estará em aspas (''), simples ou duplas. 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FATIAMENTO DE STRINGS

frase = "Curso em Vídeo python"

print(frase[9]) #irá imprimir somente a letra que corresponde ao número 9. lembrando que sempre começa em zero (0)

print(frase[9:13]) #aqui, ele irá do 9 até o 13, porém irá excluir a letra número 13.  Isso é chamado de range.

#Outro exemplo de fatiamento:

print(frase[9:21:2]) #o terceiro parâmetro vai fazer com que pule de dois em dois. 

print(frase[:5]) #ele vai definir onde vai parar. antes dos dois pontos ele vai pegar do começo, e após os dois pontos é onde vai parar. 

print(frase[9::3]) #o 9 indica onde ele vai começar, já o espaço vazio entre os dois pontos vai dizer que ele vai pegar até o final. o 2 significa que vai pular de 3 em 3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ANÁLISE DE STRING

len(frase) #len significa comprimento, e ele vai descobrir o comprimento (qnt de letras) da frase

frase.count('o') #vai contar quandas vezes aparece a letra "o" minúscula

frase.count('o', 0, 13) #os outros parâmetros vão definir de onde começa e onde termina. 

frase.find('deo') #vai procurar dentro da var o que está escrito dentro do parâmetro

frase.find('Android') #ele vai retornar o valor '-1', que significa que o programa não encontrou nenhuma string 'android' (ou seja lá qual for) dentro da váriavel

'Curso' in frase #significa: em(in) frase existe 'curso'? E ele retornará um valor True ou False 

frase.replace('Python', 'Android') #Ele irá trocar o item do primeiro parâmetro pelo item do segundo parâmetro. 

frase.upper() #Ele vai transformar todas as frases em maíusculo. 

frase.lower() #Transformará as frases em minúsculas. 

frase.capitalize() #Vai pegar toda a string e vai mandar pra minúsculo, e manterá apenas a primeira letra de cada palavra em maiúscula. 

frase.tittle() #vai analisar quantas palavras tem na string

frase.strip() #vai remover os espaços inúteis no começo e no final da string 

frase.rstrip() #vai remover somente os últimos espaços (o 'r' sifnifica right, ou direita) 

frase.lstrip() #vai remover somente os primeiros espaços (o 'L' sifnifica left, ou esquerda)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#DIVISÃO DE STRINGS

frase.split() #vai dividir a string exatamente onde existir espaços. cada palavra será recebida em uma nova lista recem criada

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#JUNÇÃO DE STRINGS

'-'.join(frase) #ele vai mudar todos os espaços pelo que for definido dentro das aspas simples 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#UTILIZAR AS ASPAS TRIPLAS FARÁ COM QUE O TEXTO MANTENHA A FORMATAÇÃO ORIGINAL, ASSIM COMO ESTÁ EXEMPLIFICADO ABAIXO. 

print("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ATIVIDADES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#01 - Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

a = input('Digite o seu nome completo: ').strip()

print(f'O seu nome todo maiúsculo ficará assim: {a.upper()}') #tudo maiusculo
print(f'O seu nome todo minusculo ficará assim: {a.lower()}') #tudo minusculo
print('O seu nome possui {} letras.' .format(len(a) - a.count(' '))) #conta quantas letras tem excluindo os espaços
print('O primeiro nome tem {} letras.' .format(a.find(' ')))  #conta quantas letras tem na primeira palavra
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#02 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: 1834. Unidade: 4 | Dezena: 3 | centenas: 8 | Milhar: 1

a = int(input('Digite um número inteiro de 0 a 9999: '))

m = a // 1000 % 10  #milhar
c = a // 100 % 10   #centena
d = a // 10 % 10    #dezena
u = a // 1 % 10     #unidade

print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#03 - Crie um programa que leia o nome de uma cidade e diga se ela começa sim ou não com o nome "Santo"

a = str(input('Digite o nome da cidade: ')).strip() #Strip irá eliminar todos os espaços desnecessários da string
print(a[:5].upper() == "SANTO" ) #verificará se o resultado é igual a 'SANTO'

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#04 - Crie um programa que leia o nome de uma pessoa e diga se ela possui "Silva" no nome

a = str(input('Digite o seu nome completo: ')).strip()
a = a.upper()
b = 'SILVA' in a
print(f'O seu nome tem Silva? {b}')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#05 - Crie um programa que leia uma frase pelo teclado e mostre: 
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece pela primeira vez
#Em qual posição ela aparece pela última vez. 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#06 - Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o seu primeiro e o seu último nome separadamente. 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

