#ATIVIDADE 01 - DE PROCURAR PREÇO COM DESCONTO
preco = float (input('Digite o valor do produto:'))
p = float (input('Digite o percentual de desconto (0-100)%: '))

desconto = preco * (p/100)
final = preco - desconto

print('O valor do produto é: {} reais. O desconto aplicado será de: {}' .format(preco, p))
print('O valor do produto com o desconto aplicado é de {}, com um desconto de {}%.' .format(final, desconto))








































#ATIVIDADE 02 DE DESCOBRIR A KILOMETRAGEM 
km = int(input ('Quantos KM foram percorridos?'))
dias = int(input('Por quantos dias você alugou este carro?'))

preco = 60 * dias + 0.15 * km

print('O carro foi alugado por {} dias e foram percorridos {}Km.' .format(dias, km))
print('O valor do aluguel é de: {} reais.' .format(preco))




#ATIVIDADE 03 DE CORTAR UMA FRASE AO MEIO

frase = input('Digite uma frase qualquer aqui:')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])

