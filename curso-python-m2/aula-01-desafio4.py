#Desafio 04 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 
#Se ele ainda vai se alistar ao serviço militar. ☺
#Se é a hora de se alistar.☺
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
nascimento = int(input('Em que ano você nasceu? '))

data = date.today()
ano = int(f'{data.year}') 
idade = ano - nascimento 

if idade < 18:
    tempo_restante = 18 - (ano - nascimento)
    print(f'Por possuir apenas {idade} anos, você ainda não precisa se alistar. Faltam exatamente {tempo_restante} ano(s) para você se alistar.')

elif idade == 18:
    tempo_restante = 18 - (ano - nascimento)
    print(f'Você possui {idade} anos e está na idade de se alistar.')

elif idade >= 19:
    print(f'Você já passou da idade de se alistar. Já se passou {(ano - nascimento) - 18} ano(s) do seu prazo de alistamento.')