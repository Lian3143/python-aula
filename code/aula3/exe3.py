## ESCOLHAS
print('O que você vai querer?')
print('1 - Maçã')
print('2 - Banana')
print('3 - Laranja')
# INPUT PARA ESCOLHER O QUE QUERER
item = int(input('Qual item você irá escolher?'))
qnt = int(input('Quantas você vai querer?'))
# OPERADOR LÓGICO
if (item == 1):
    valor = qnt * 2.30
    print('O valor a se pagar é de {} reais.'.format(valor))
else:
    if (item == 2):
        valor = qnt * 1.85
        print('O valor a se pagar é de: {} reais.' .format(valor))
    else:
        if (item == 3):
            valor = qnt * 3.6
            print('O valor a se pagar é de {} reais.' .format(valor))
        else:
           print('Produto inexistente!')

# ------------------------------------------------------------------------------------
print('O que você vai querer?')
print('O que você vai querer?')
print('1 - Maçã')
print('2 - Banana')
print('3 - Laranja')
# INPUT PARA ESCOLHER O QUE QUERER
item = int(input('Qual item você irá escolher?'))
qnt = int(input('Quantas você vai querer?'))
# OPERADOR LÓGICO
if (item == 1):
    valor = qnt * 2.30
    print('O valor a se pagar é de {} reais.'.format(valor))
elif (item == 2):
    valor = qnt * 1.85
    print('O valor a se pagar é de: {} reais.' .format(valor))
elif (item == 3):
    valor = qnt * 3.6
    print('O valor a se pagar é de {} reais.' .format(valor))
else:
    print('Produto inexistente!')
