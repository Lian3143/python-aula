from random import choice
print('Aqui está a sua lista de jogadas: ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogada = int(input('Qual será a sua jogada? '))

pc_jogadas = ["pedra", "papel", "tesoura"]
pc_escolha = choice(pc_jogadas)

if jogada == 1:
    print(f'Você escolheu pedra.\nAgora, é hora do computador escolher...\nO computador escolheu {pc_escolha}!')
    if pc_escolha == "pedra":
        print(f'A máquina escolheu {pc_escolha}, portanto, a partida está empatada!')
    else: 
        print('Você ganhou!')
elif jogada == 2:
    print(f'Você escolheu pedra.\n Agora, é hora do computador escolher...\nO computador escolheu {pc_escolha}!')
    if pc_escolha == "papel":
        print(f'A máquina escolheu {pc_escolha}, portanto, a partida está empatada!')
    else: 
        print('Você ganhou!')

elif jogada == 3:
    print(f'Você escolheu pedra.\n Agora, é hora do computador escolher...\nO computador escolheu {pc_escolha}!')
    if pc_escolha == "tesoura":
        print(f'A máquina escolheu {pc_escolha}, portanto, a partida está empatada!')
    else: 
        print('Você ganhou!')

print('Obrigado por participar do nosso jogo! \nEncerrando programa...')

