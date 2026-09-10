'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
Ao final deve mostrar a quantidade de vitórias
'''

# Importa o módulo random, que permite gerar números aleatórios
import random

# Cria uma variável para contar quantas vezes o jogador venceu
vitoria = 0

# Cria um loop infinito. O jogo continuará até acontecer um "break"
while True:

    # Pede para o jogador escolher PAR ou ÍMPAR
    # .strip() → remove espaços antes/depois do que foi digitado
    # .upper() → transforma a resposta em letra maiúscula
    # [0] → pega apenas o primeiro caractere
    escolha = input('PAR ou ÍMPAR [P/I]: ').strip().upper()[0]

    # Continua perguntando enquanto a escolha não for P ou I
    while escolha not in 'PI':

        # Pede novamente a escolha e aplica as mesmas transformações
        escolha = input('PAR ou ÍMPAR [P/I]: ').strip().upper()[0]


    # Pede para o jogador escolher um número
    # int() transforma o que foi digitado de texto para número inteiro
    jogador = int(input('Dígite um número de 1 a 10: '))

    # Verifica se o número está fora do intervalo permitido
    while jogador < 1 or jogador > 10:

        # Se estiver fora de 1 a 10, pede novamente
        jogador = int(input('Dígite um número de 1 a 10: '))


    # O computador escolhe aleatoriamente um número entre 1 e 10
    pc = random.randint(1, 10)


    # Soma o número do jogador com o número do computador
    # % 2 calcula o resto da divisão por 2
    #
    # Se o resto for 0 → a soma é PAR
    # Se o resto for diferente de 0 → a soma é ÍMPAR
    #
    # A primeira parte verifica:
    # "A soma é PAR e o jogador escolheu P?"
    #
    # A segunda parte verifica:
    # "A soma é ÍMPAR e o jogador escolheu I?"
    #
    # O "or" significa que basta uma das duas condições ser verdadeira
    if ((jogador + pc) % 2 == 0 and escolha == 'P') or ((jogador + pc) % 2 != 0 and escolha == 'I'):

        # Mostra que o jogador venceu
        print('Vitória Jogador!!!!')

        # Aumenta a quantidade de vitórias
        vitoria += 1

    else:

        # Se a condição acima não for verdadeira, o jogador perdeu
        print('Ixi, perdeu!')

        # Encerra o loop e, consequentemente, o jogo
        break



