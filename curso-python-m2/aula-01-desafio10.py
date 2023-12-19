
from random import choice

escolha_jogador = str(input('Qual será a sua jogada? Pedra, papel ou tesoura? ')).strip().lower() #jogador escolherá a sua jogada
jogadas = ['pedra', 'papel', 'tesoura'] #lista delimitando as jogadas
pc_escolha = choice(jogadas) #choice irá escolher um item da lista

if escolha_jogador not in jogadas:  #vai limitar as escolhas somente aos itens que estão dentro da lista "jogadas"
    print('Opção inválida.\nTente novamente!')

elif escolha_jogador == pc_escolha: #vai avisar quando for empate!
    print(f'Você escolheu: {escolha_jogador}. \nA máquina escolheu: {pc_escolha}.')
    print('Empate!')

elif ((escolha_jogador == 'pedra' and pc_escolha == 'tesoura') or #vai definir quem é maior e quem é menor
        (escolha_jogador == 'papel' and pc_escolha == 'pedra') or
        (escolha_jogador == 'tesoura' and pc_escolha == 'papel')):
    print(f'Você escolheu: {escolha_jogador}. \nA máquina escolheu: {pc_escolha}')
    print('Você venceu!')
else:
    print(f'Você escolheu: {escolha_jogador}. \nA máquina escolheu: {pc_escolha}')
    print('Você perdeu!')

