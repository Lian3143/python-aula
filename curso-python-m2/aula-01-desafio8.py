#Desafio 08 - Desenvolva uma lógica que leia o peso e a altura  de uma pessoa, calcule seu IMC e mostre o seu status, de acordo com a tabela abaixo. 
#Abaixo de 18.5 - abaixo do peso ☺
#entre 18.5 e 25 - peso ideal ☺
#entre 25 e 30 - acima do peso
#entre 30 e 40 - obesidade
#acima de 40 - obesidade mórbida

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))

calc = peso/(altura)**2

if calc <= 18.5:
    print(f'O seu IMC é {calc:.2f}. Você está abaixo do peso.')

elif calc >= 18.5 and calc <= 25:
    print(f'O seu IMC é {calc:.2f}. Você está no peso ideal.')

elif calc >= 25 and calc <= 30:
    print(f'O seu IMC é {calc}. Você está acima do peso.')

elif calc >= 30 and calc <= 40:
    print(f'O seu IMC é {calc}. Você está com obesidade.')

elif calc >= 40:
    print(f'O seu IMC é {calc}. Você está com obesidade mórbida.')

