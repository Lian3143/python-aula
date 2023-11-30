
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Erro! Divisão por zero.'
    else:
        return a / b

def calculadora():
    while True:
        print('\Selecione a operação:')
        print('1. Adição')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('5. Sair')
        escolha = input('Digite 1, 2, 3, 4, 5: ')

        if escolha == '5':
            print('Finalizando calculadora...')
            break

        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))

        if escolha == '1':
            print('Resultado:', adicao(num1, num2))
        elif escolha == '2':
            print('Resultado:', subtracao(num1, num2))
        elif escolha == '3':
            print('Resultado:', multiplicacao(num1, num2))
        elif escolha == '4':
            print('Resultado:', divisao(num1, num2))
        else:
            print('Escolha inválida. Por favor, escolha 1, 2, 3, 4 ou 5.')

calculadora()