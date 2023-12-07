#07 - Faça um programa que leia a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m**2 

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print(f'A sua parede tem a dimensão de {larg}x{alt}, e uma área de {area}.\nPara pintar essa parede, você precisará de {area/2} litros de tinta.')