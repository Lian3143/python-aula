#3 - Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

#aleatorizando as jogadas da máquina
from random import randint

pc_escolha = randint(1, 10)


#variáveis de apoio
vitorias = 0
#loop central
while True:
    # escolhas do jogador
    print(f'Pc escolha: {pc_escolha}')
    player_escolha = str(input('Escolha uma jogada (impar ou par): ')).strip().lower()
    player_valor_escolha = int(input(f'Escolha um valor (1-10): '))

    #checando vencedor
    if player_escolha == 'impar':
        print('Você escolheu impar.')
        soma = player_valor_escolha + pc_escolha
        if soma % 2 == 0:
            print(f'Você perdeu! {pc_escolha} + {player_valor_escolha} é igual a {soma}, e {soma} é par.')
            break
        else:
            vitorias += 1
            print(f'Você venceu! Agora você está com {vitorias} vitórias!')
    elif player_escolha == 'par':
        print('Você escolheu par.')
        soma = player_valor_escolha + pc_escolha
        if soma % 2 == 0:
            vitorias += 1
            print(f'Você venceu! Agora você está com {vitorias} vitórias!')
        else:
            print(f'Você perdeu! {pc_escolha} + {player_valor_escolha} é igual a {soma}, e {soma} é impar.')
            break

    #print com o resultado
print(f'Finalizando a partida. Você ganhou um total de {vitorias} rodadas. ')



