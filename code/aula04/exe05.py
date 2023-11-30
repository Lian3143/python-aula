nome = input('Digite seu nome:')
print(f'Seja bem-vindo, {nome}!')
while True: 
    print('Qual operação você deseja realizar?')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')
    op = input('Digite qual operação deseja realizar de acordo com as opções acima:')
    if op == '5':
        print('Opção "Sair" selecionada.')
        break
    v1 = float(input('Digite o primeiro valor:'))
    v2 = float(input('Digite o segundo valor:'))

    if op == '1':
        calc = v1+v2
        print(f'{v1} + {v2} = {calc}')
        continue
    elif (op == '2'):
        calc = v1-v2
        print(f'{v1} - {v2} = {calc}')
        continue
    elif (op == '3'):
        calc = v1 * v2
        print(f'{v1} x {v2} = {calc}')
        continue          
    elif (op == '4'):
        calc = v1 / v2
        print(f'{v1}/{v2} = {calc}')
        continue
    else:
        print('Valor inválido. Tente novamente.')
        continue

print('Encerrando programa...')


#------------------------------------- QUESTAO 2
valor = int(input('Digite o valor em reais:'))

while True:
    if (valor >= 100):
        cedulas100 = valor // 100
        valor -= cedulas100 *100
        print(f'Cédulas de 100: {cedulas100}')
        if not valor:
            break
    if (valor >= 50):
        cedulas50 = valor // 50
        valor -= cedulas50 *50
        print(f'Cédulas de 50: {cedulas50}')
        if not valor:
            break
    if (valor >= 20):
        cedulas20 = valor // 20
        valor -= cedulas20 *20
        print(f'Cédulas de 20: {cedulas20}')
        if not valor:
            break
    if (valor >= 10):
        cedulas10 = valor // 10
        valor -= cedulas10 *10
        print(f'Cédulas de 10: {cedulas10}')
        if not valor:
            break
    if (valor >= 5):
        cedulas5 = valor // 5
        valor -= cedulas5 *5
        print(f'Cédulas de 5: {cedulas5}')
        if not valor:
            break
    if (valor):
        cedulas1 = valor
        print(f'Cédulas de 1: {cedulas1}')
        break
        