from random import choice

jogadas = ['Pedra!', 'Papel!', 'Tesoura!']

pc_jogada = choice(jogadas)

print('-=-|'*5,'Opções para o jogador', '-=-|'*5)

print(' (1) - Pedra\n (2) - Papel\n (3) - Tesoura ')
print('-=-|'*16,)

player_jogada = int(input('Qual será a sua jogada? '))

if player_jogada == 1:
    print(f' A sua jogada foi: Pedra!\n A jogada do pc foi: {pc_jogada}')
    if pc_jogada == 'Pedra!':
        print(" Empate!")
    elif pc_jogada == 'Papel!':
          print(f'Você perdeu! :(')
    elif pc_jogada == 'Tesoura!':
        print('Parabéns! Você venceu! :D')

elif player_jogada == 2:
        print(f' A sua jogada foi: Papel!\n A jogada do pc foi: {pc_jogada}')
        if pc_jogada == 'Pedra!':
            print(" Parabéns! Você venceu! :D")
        elif pc_jogada == 'Papel!':
            print(f' Empate!')
        elif pc_jogada == 'Tesoura!':
            print(' Você perdeu! :( ')

elif player_jogada == 3:
        print(f' A sua jogada foi: Tesoura!\n A jogada do pc foi: {pc_jogada}')
        if pc_jogada == 'Pedra!':
            print(" Você perdeu! Tente novamente! :( ")
        elif pc_jogada == 'Papel!':
            print(f' Parabéns! Você venceu! :D')
        elif pc_jogada == 'Tesoura!':
            print(' Empate!')

print('Encerrando programa...')
