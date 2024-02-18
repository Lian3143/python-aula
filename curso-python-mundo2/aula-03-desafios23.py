#2 - Melhore o desafio028 onde o computador vai "pensar" em um número de entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import choice

#variáveis de apoio
maquina_jogadas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha_maquina = choice(maquina_jogadas) #aleatoriezando a escolha da máquina
jogador_escolha = 0
jogada_inicial = int(input('Você começa! De 1 a 10, qual número você acha que eu escolhi? '))
print(escolha_maquina)
erros = 0 #total de palpites do jogador


#laço de repetição
while jogador_escolha != escolha_maquina:
    if jogador_escolha != maquina_jogadas:
        print('Número inválido. Por favor, tente novamente utilizando apenas números inteiros de 1 à 10. ☺')

    #verificando se o jogador errou. Se errou, irá repetir o loop até acertar..
    print(f'Você errou! Tente novamente!')
    jogador_escolha = int(input('Qual será o seu próximo palpite? '))
    erros += 1

    # verificando se o jogador ganhou
    if jogada_inicial == escolha_maquina or jogador_escolha == escolha_maquina:
        print(f' Parabéns, você venceu!')
        if erros < 3:
            print(f'Você precisou de apenas {erros} para acertar a minha escolha! Você é bom nisso!')

        elif erros < 6:
            print(f'{erros} jogadas? Você até que é bom. ')

        elif erros >= 10:
            print(f'{erros} jogadas? Acho que você precisa praticar um pouquinho...')

#print para encerrar o programa.
print('Obrigado por participar do nosso jogo! Volte sempre que quiser! ♥\nEncerrando programa...')