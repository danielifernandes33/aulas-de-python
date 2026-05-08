"""
Escreva um programa que verifique se uma frase é um palíndromo.
"""

#Entrada de dados: 
frase = input('Digite uma frase: ').strip().upper().replace(' ','')

#1
compatibilidade = 0

for i in range(0,len(frase)):
    if frase[i] == frase[-i -1]:
        compatibilidade +=1

if compatibilidade == len(frase):
    print('É um palíndromo')

else:
    print('Não é um palíndromo')

#2
if frase == frase[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

