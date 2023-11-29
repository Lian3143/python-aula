def validando_int(pergunta, min, max):
    x = input(pergunta)
    tam = len(x)
    while (tam < 0) or (tam > 3):
        x = input(pergunta)
        return x


def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close
    except:
        print('Erro na seleção de arquivo.')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso! \n')


def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True


def listar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'r')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()


def cadastrar_jogo(nome_arquivo, nome_jogo, nome_videogame):
    try:
        a = open(nome_arquivo, 'at')
        a.close
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nome_jogo}; {nome_videogame} \n')
    finally:1
        a.close()


# Principal

arquivo = 'games.txt'

if existe_arquivo(arquivo):
    print('Arquivo localizado!')
else:
    print('Arquivo inexistente!')
    criar_arquivo(arquivo)

while True:
    print('Menu')
    print('1. Cadastrar um novo item')
    print('2. Listar itens existentes')
    print('3. Sair')

    op = validando_int('Escolha a opção desejada: ', 1, 3)

    if (op == '1'):
        print('Opção de cadastro de um novo item selecionada. \n')
        nome_jogo = input('Digite o nome do jogo:')
        nome_videogame = input('Digite o nome do videogame:')
        cadastrar_jogo(arquivo, nome_jogo, nome_videogame)
    elif (op == '2'):
        print('Opção de listagem de itens existentes selecionada. \n')
        listar_arquivo(arquivo)
    elif (op == '3'):
        print('Opção "Sair" selecionada. \n Finalizando programa...')
        break