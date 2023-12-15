#04 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.

km = int(input('Digite quantos KM serão percorridos na viagem: '))

if km <= 200: #vai comparar se km é igual ou menor a 200. 
    print(f'Ao percorrer {km}KM, você terá que pagar {km*0.50:.2f} na passagem.')
else:
    print(f'Ao percorrer {km}KM, você terá que pagar {km*0.45:.2f} na sua passagem.')

print('Boa viagem!')