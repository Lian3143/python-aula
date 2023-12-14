#05 - Crie um programa que leia uma frase pelo teclado e mostre: 
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece pela primeira vez
#Em qual posição ela aparece pela última vez. 

a = str(input('Digite uma frase qualquer: ')) .strip()
print(f'A letra "a" aparece {a.count("a")} vezes.')
print(f'Ela aparece primeiro na posição #{}')