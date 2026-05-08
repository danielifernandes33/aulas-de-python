'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez
'''

#Entrada de dados:
frase = input('Digite uma frase: ').strip().lower()

frase = frase.replace('á','a')
frase = frase.replace('à','a')
frase = frase.replace('â','a')
frase = frase.replace('ã','a')
frase = frase.replace('ä','a')

#Conta a quantidade de vezes que a letra "a" apareceu na frase:
qtd_letra_a = frase.count(('a'))  #frequência de um determinado caracter

#Qual a posição do primeiro A na frase?
primeiro_a = frase.find('a')

#Qual a posição do último A na frase?
ultimo_a = frase.rfind('a')

#Saída de dados:

print(f'Quantas vezes apareceu a letra A na frase: {qtd_letra_a}'
      f'\nQual é a posição do primeiro A: {primeiro_a}'
      f'\nQual é a posição do último A: {ultimo_a}')




