#MUNDO DOIS DO CURSO DE PYTHON
#DICAS E REGRAS!
#ESTRUTURAS DE CONTROLE, CONDIÇÕES E LAÇOS | MUNDO 2

#AULA TEÓRICA, ESTRUTURAS DE REPETIÇÃO (WHILE, for e elif)

#Aula - 01 | Estruturas de repetição 

#elif pode ser usado quantas vezes quiser dentro de um if. Porém, não pode ser usado sem um if. 
#Else só pode ser utilizado uma única vez ou nenhuma vez. 

#Aula prática - 01

#Aqui um exemplo de condição simples, onde apenas um IF é utilizado. 
nome = str(input('Qual o seu nome?')).strip()

if nome == 'Lian':
    print(f'Que nome bonito, {nome}!')
print(f'Tenha um bom dia, {nome}!') 

#Aqui um exemplo de condicional composta, onde é utilizado um if e um else

nome = str(input('Qual o seu nome?')).strip()

if nome == 'Lian':
    print(f'Que nome bonito, {nome}!')
else:
    print(f'Seu nome é bem comum.')
print(f'Tenha um bom dia, {nome}!') 

#Aqui está um exemplo de uma condicional aninhada utilizando if, else e elif. 

nome = str(input('Qual o seu nome?')).strip()

if nome == 'Lian':
    print(f'Que nome bonito, {nome}!')
elif nome == 'Gustavo':
    print(f'Seu nome é bem diferente{nome}.')
else:
    print(f'Seu nome é bem comum.')
print(f'Tenha um bom dia, {nome}!') 
