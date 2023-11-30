
#--------
dano = int(input('Quanto de dano será dado? (0-10)'))
escudo = int(input('Qual a durabilidade do escudo? (0-10)'))
if (dano > 10 and escudo == 0):
  print('Você está morto')




#--------
norte =  print('Você escolheu este caminho!')
sul = print('Você escolheu este caminho!')
leste = print('Você escolheu este caminho!')
oeste = print('Você escolheu este caminho!')
if (norte or sul or leste or oeste):
  print('Você escapou!')


#========= condicional composta ======== 
#LETRA A
ano = int(input('Digite o ano:'))
if ano % 4 == 0: 
    print('Pode ser um ano bisexto!')
else: 
    print('Não pode ser um ano bisexto!')

#letra b

cima = True
baixo = True  # Defina o valor de cima e baixo como True ou False conforme necessário

if cima and baixo:
    print("Decida-se!")
else:
    print("Você escolheu um caminho")


#####################

kwh = float(input('Quantos KWH foram consumidos?'))

print('Escolha o tipo de instalação:')
print('R - Residencial')
print('C - Comercial')
print('I - Industrial')
tipo = input('Qual o tipo da sua instalação?')

if tipo == 'R' and tipo == 'r':
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'C' and'c':
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'i' and 'I':
    if kwh <= 5000:
        preco = 0.55
    else: 
        preco = 0.60
else:
    print('Digite um caractere válido.')

print('O valor a se pagar é: {}.' .format(kwh*preco))