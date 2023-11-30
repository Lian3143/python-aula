# variaveis
media = 7  # média para ser aprovado
mat = float(input('Digite a sua nota:'))
pt = float(input('Digite a sua nota:'))
en = float(input('Digite a sua nota:'))

# comparação
if mat >= media and pt >= media and en >= media:
    print('Parabéns! Você está aprovado!')  # resultadoA
else:
    # resultadoB
    print('Infelizmente você não obteve a prontuação necessária para ser aprovado.')


texto = 'Olá, mundo!'

tam = len(texto)
print(tam)
print(texto[0:4])
