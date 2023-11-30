nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

if nome == 'Vinicius':
    print('Olá, Vinicius! Seja bem-vindo!')
elif idade < 18:
    print('Você é menor de idade e não é Vinicius!')
elif idade > 100:
    print('Você é imortal? Essa idade não é válida.')
