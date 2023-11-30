num1 = float(input('Digite o primeiro número:'))
op = input('Qual operação deseja fazer?')
num2 = float(input('Digite o segunto número:'))

if (op == '+'):
    resultado = num1 + num2
    print('{}+{} é igual a: {}' .format(num1, num2, resultado))
elif (op == '-'):
    resultado = num1-num2
    print('{}-{} é igual a: {}' .format(num1, num2, resultado))
elif (op == '*'):
    resultado = num1*num2
    print('{}x{} é igual a: {}' .format(num1, num2, resultado))
elif (op == '/'):
    resultado = num1/num2
    print('{}/{} é igual a: {}' .format(num1, num2, resultado))
