"""
Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
"""

#Entrada de dados:
idade = float(input('Qual a sua idade? '))
peso = float(input('Qual o seu peso? '))
bebida_alcoolica = input('Consumiu bebida alcoólica nas últinas 12 horas? ').strip().lower()
comida_gordurosa = input('Consumiu comida gordurosa nas últinas 4 horas? ').strip().lower()
tatuagem = input('Fez alguma tatuagem nos últinos 12 meses? ').strip().lower()

if idade (<= 16 and idade >=56) ou (bebida_alcoolica == sim):
    print('N Pode doar sangue')
elif peso < 50:
    print('N Pode doar sangue')
elif bebida_alcoolica > sim:
    print('N Pode doar sangue')
elif comida_gordurosa > sim:
    print('N Pode doar sangue')
elif tatuagem > sim:
    print('N Pode doar sangue')
else:
    print('Pode doar dessa vez.')