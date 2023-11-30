soma = 0
cont = 1
while (cont <=5): #repetição
    x = float(input(f'Digite {cont}° nota:'))
    soma += x #Equivalente a: soma = soma + x
    cont += 1 #Equivalente a: cont = cont + 1
media = soma / 5
print(f'Média final: {media}')
if (media >= 5):
    print('Aprovado!')
else:
    print('Reprovado')