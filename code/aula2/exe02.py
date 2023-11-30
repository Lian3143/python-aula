#Questão um

preco = float(input('Digite o valor do produto:'))
p = float(input('Digite o desconto que será aplicado:'))
desconto = preco * (p/100)
final = preco - desconto
print('O valor do produto é de {} e o desconto de {}.' .format(preco, p))
print ('O valor do produto com desconto é de {} reais. Houve um desconto de {} reais.' .format(final, desconto))
 
 
 #Questão dois 


km = int(input('Quantos KM foram percorridos pelo veículo?'))
dias = int(input('O veículo ficou alugad por quantos dias?'))
preco = dias * 60 + km * 0.15

print('O carro ficou alugado por {} dias, rodando um total de {}KM.' .format(dias, km))
print('O valor a se pagar pelo aluguel é de: {} reais.' .format(preco))

#Questão três! 

frase = input('Digite uma frase qualquer:')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])