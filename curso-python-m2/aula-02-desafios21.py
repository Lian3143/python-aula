#11 - Desenvolva um program que leia nome, idade e sexo de 4 pessoas. No final, mostre:
#A média de idade do grupo
#Qual o nome do homem mais velho.
#Quantas mulheres tem menos 20 anos
#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=--=--=--=--=--=-

#variáveis de apoio
mais_velho = 0
nome_mais_velho = ''
mulheres_menos_20 = 0
media_idade = 0
idade_total = 0

#estrutura de repetição.
for i in range(1, 5):
    print(f'=--=- {i}ª Pessoa -=--=')
    nome = str(input(f'Digite o {i}° nome: ')).strip()
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}ª pessoa: ')).strip().upper()

#calculando a média de idade
    idade_total += idade
    media_idade = (idade_total/4)

#verificando quantas mulheres possuem menos de 20 anos
    if sexo == 'F' and idade <= 20:
       mulheres_menos_20 += 1

#verificando o nome do homem mais velho
    if sexo == 'M':
        mais_velho == idade

    if sexo == 'M' and idade >= mais_velho:
        mais_velho = idade
        nome_mais_velho = nome

#Print com o resultado
print('-=-'*20)

print(f' A média de idade do grupo é {media_idade:.2f} anos.'
      f'\n O nome do homem mais velho é {nome_mais_velho} e ele possui {mais_velho} anos.')
if mulheres_menos_20 == 0:
    print(f' Nenhuma mulher cadastrada possui 20 anos ou menos. ')
elif mulheres_menos_20 == 1:
    print(f' Apenas uma mulher possui 20 anos ou menos.')
else:
    print(f' Um total de {mulheres_menos_20} mulheres possuem menos de 20 anos. ')

print('-=-' * 20)