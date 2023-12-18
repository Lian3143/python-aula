#Desafio 04 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 
#Se ele ainda vai se alistar ao serviço militar. 
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
nascimento = int(input('Em que ano você nasceu? '))

data = date.today()
ano = '{}' .format(data.year)

if nascimento < ano:
    tempo_restante = (nascimento - ano) - 18
    print(f'Por possuir apenas {nascimento - ano} anos, você ainda não precisa se alistar. Faltam exatamente {tempo_restante} anos para você se alistar.')