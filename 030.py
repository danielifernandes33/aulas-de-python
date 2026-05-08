'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
Ao final deve mostrar a quantidade de vitórias
'''


import random

pc = random.randint(1,10)
escolha = int(input('Digite 1 - para escolher PAR - 2 - para escolher ÍMPAR'))

jogador = int(input('Dígite um número de 1 a 10'))
vitorias = 0


while True:
    if (escolha == 1 and (jogador + pc) % 2 == 0) or (escolha == 2 and (jogador + pc) % 2 != 0):
        print('Vitória Jogador')
        vitorias = vitorias + 1

    else:
        print('perdeu')




