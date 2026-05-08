'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue
pedindo até que o usuário acerte o número.
E no final, retorne também a quantidade de tentativas necessárias.
'''


import random

numero_pc = random.randint(1,10)
numero_jogador = int(input('Digite um número de 1 a 10: '))
tentativas = 1

while numero_jogador != numero_pc:
    print('Você errou! Tente novamente')
    numero_jogador = int(input('Digite um número de 1 a 10: '))
    tentativas +=1

print('Você acertou! Miserável!!!!'
      f'\nQuantidade de tentativas: {tentativas}')




