'''
Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.
'''

#Entrada de dados:
numero = float(input('Digite um número: '))

if numero >= 0:
    print('Número positivo')
elif numero == 0:
    print('Número neutro')
else:
    print("não é par")
