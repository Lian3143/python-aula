#LISTAS
mochila_normal = ['Sabonete', 'camisa', 'banana'] #UTILIZA COLCHETE PARA CRIAR UMA LISTA 
upgrade = ['Bacon', 'canivete'] #PODEMOS ALTERAR OS DADOS DE UMA LISTA COM FACILIDADE

mochila_grande = mochila_normal + upgrade 

#EX DE ALTERAÇÃO

mochila = ['Banana', 'maça', 'pera', 'laranja', 'uva']
mochila[3] = 'ABACATE'

print('Lista: ', mochila)

#outras maneiras de alterar itens em uma lista

mochila.append('Ovos') #vai inserir o item no final da lista, basta adicionar o .append dps do nome da VAR

mochila.insert(2,'canivete') #vai inserir o item no lugar em que você desejar, basta colocar insert e, antes do item que vc quer add, colocar um parâmetro dizendo onde quer colcoar

del mochila[1]
print('Lista: ', mochila)
mochila.remove('Ovos')
print('Lista: ', mochila)
#DELETA ITENS DA LISTA. REMOVE SERVE PRA DELETAR QUAO ITEM EU QUERO, E O DEL SERVE PRA REMOVER POR MEIO DO INDICE

#CRIANDO LISTAS NUMÉRICAS
x = [1,2,3,4,5]
y = x

y[0] = 3 #SE EU TENTAR ALTERAR APENAS O Y, ELE VAI ALTERAR AMBOS. COMO RESOVER? 

#CÓPIA
x = [1,2,3,4,5]
y = x[:]

y[0] = 3
#ASSIM ELE CRIA UMA CÓPIA DE 'X' NA MEMÓRIA, E AO TENTAR ALTERAR ELE IRÁ ALTERAR APENAS O ÍNDICE 0 NA VÁRIALVEL Y E X CONTINUARÁ IGUAL