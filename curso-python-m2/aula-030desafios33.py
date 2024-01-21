#3 - Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

#aleatorizando as jogadas da máquina
from random import randint

pc_escolha = randint(1, 50)
print(pc_escolha)

#variáveis de apoio
cont = 0
vitorias = 0
derrotas = 0

#loop central
while True:
    # escolhas do jogador
    player_escolha = str(input('Escolha uma jogada (impar ou par): ')).strip().lower()
    player_valor_escolha = int(input(f'Escolha um valor (1-50): '))

    #checando vencedor




