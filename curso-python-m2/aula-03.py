#ESTRUTURA WHILE (MESMA COISA QUE O FOR, PORÉM COM FUNÇÕES DIFERENTES)
#é chamada de estrutura de repetição com teste lógico.
#While é utilizado quando não se sabe um valor para começar e encerrar o laço.
#while é um loop infinito.
#é importante ficar atento à identação do laço, igual o for

#Exemplos e diferenças entre for e while

"""for i in range(1,10):
    print(i)
print('Fim')"""

#-----------------------------------
'''i = 0
while i < 10:
    print(i)
    i += 1
print('Fim')'''

#Quando se sabe um limite, o for e o while pode ser usados igualmente. Porém quando um limite não é definido, o while se torna uma opção melhor.
#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
#Exemplo utilizando o for e utilizando um valor pré-definido.

''' for i in range(1, 6):
    input(f'Digite o {i}° valor: ')
print('Fim') '''

#exemplo utilizando o while e sem um valor pré-definido.
'''
i = 1
while i != 0:
    i = int(input(f'Digite um valor: '))
print('Fim')'''

#Ambos os códigos possuem o mesmo fazem a mesma coisa, porém no while não há um valor pré-definido para o código ser encerrado.

#Exemplo 3 (verificando se um número é ímpar ou par utilizando while

'''c = 1
par = impar = 0

while c != 0:
    c = int(input('Digite um valor: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} valores pares e {impar} valores impares.')'''








