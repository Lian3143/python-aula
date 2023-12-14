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

'Curso' in frase #significa: em(in) frase existe 'curso'? E ele retornará um valor 

frase.replace('Python', 'Android') #Ele irá trocar o item do primeiro parâmetro pelo item do segundo parâmetro. 

frase.upper() #Ele vai transformar todas as frases em maíusculo. 

frase.lower() #Transformará as frases em minúsculas. 

frase.capitalize() #Vai pegar toda a string e vai mandar pra minúsculo, e manterá apenas a primeira letra em maiúscula. 

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
