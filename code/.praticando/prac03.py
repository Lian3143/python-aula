def validacao(pergunta, min, max):
    x = input(pergunta)
    tam = len(x)
    while (tam < 1) or (tam > 5):
        x = input(pergunta)
    return x
    
opcoes = ('1. Adição', '2. Subtração', '3. Multiplicação', '4. Divisão', '5. Sair')
nome_cliente = input('Qual seu nome?')
while True:
    print(f'Olá, {nome_cliente}. Tudo bem?')
    for item in opcoes:
        print(f'{item}')
    op = validacao('Qual Operação deseja realizar?', 1, 5)
    if (op == '5'):
        break
    else:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    if (op == '1'):
        calc = n1 + n2
        print(f'O resultado da operação é: {calc}.')
    elif (op == '2'):
        calc = n1 - n2
        print(f'O resultado da operação é: {calc}.')
    elif (op == '3'):
        calc = n1 * n2
        print(f'O resultado da operação é: {calc}.')
    elif (op == '4'):
        if n2 == '0':
            print('É impossível realizar uma divisão por zero. Tente novamente.')
    else:
        calc = n1 /n2
        print(f'O resultado da operação é: {calc}. ')