"""
Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
"""
from idlelib.replace import replace

#Entrada de Dados:
peso = float(input(('Digite o seu peso: '))) replace(',', '.')
altura = float(input(('Digite a sua altura: '))) replace(',', '.')

#Calculo IMC:

IMC = peso/altura **2

if IMC > 25:
    print('Obeso')
elif IMC > 18.5:
    print('Normal')




