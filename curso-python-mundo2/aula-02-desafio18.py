#08 - Crie um programa que leia uma frase qualquer e diga se é um políndromo, desconsiderando os espaços. 
#Exemplo: Após a sopa, de trás pra frente e desconsiderando os espaços.

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

frase = str(input('Digite uma frase: ')).strip().upper()

junto = frase.replace(' ', '')
inverso = junto[::-1]

print(f"A frase digitada foi: {junto}. E o seu inverso é: {inverso}")

if inverso == junto:
    print(f'É um políndromo. ')
else:
    print('Não é um políndromo. ')
print('Fim...\nEncerrando programa. ')    