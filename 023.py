"""
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
"""

maior_peso = None
menor_peso = None

for i in range(7):
    peso = float(input('Digite o seu peso: '))

    if menor_peso == None and maior_peso == None:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso informado é: {maior_peso}'
      f'\nO menor peso informado é: {menor_peso}')

