from datetime import date
#definindo o ano 
date = date.today().year

#maior e menor de idade
maioridade = 0
menoridade = 0

for i in range(1, pessoas_num + 1):
    ano = int(input(f'Qual o ano de nascimento da pessoa {i}? ' ))
    idade = date - ano

#Verificando quantas pessoas são menores de idade
    if idade >= 21: 
        maioridade +=1 #se a pessoa for menor de idade, vai adicionar +1 na variavel menoridade
    else:
        menoridade +=1 #se a pessoa for maior de idade, vai adicionar +1 na variavel maioridade 

#RESULTADO
print(f'Resultado:\n Um total de {maioridade} são maiores de idade.\n Já menores de idade são {menoridade} pessoas.') 
print(f'Encerrando programa...\nFim do programa. ')