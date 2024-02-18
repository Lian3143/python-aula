#04 -  Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. 

#-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

x = int(input('Para qual número você deseja verificar a tabuada? '))

for i in range(1,11): #vai repetir o loop até o 11
    print(f'Tabuada do {x}: {x} x {i} = {x*i}') #vai pegar x, que é o valor do user e multiplicar por i (que são os valores delimitados pelo loop 1-11)
    
