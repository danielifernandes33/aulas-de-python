"""
Crie um programa para jogar JOKEMPO, usando a função random.randint

Dicas

1 Gerar um número aleatório entre 1 e 3 (PC)

2 Ler um número pelo terminal entre 1 e 3 ('J'), sendo
1 = PEDRA
2 = PAPEL
3 = TESOURA

3 Compapar 'PC' e J, seguindo as regras do Jokempo, e retornar o resultado.
"""

# Inserir as bibliotecas
import time
import random

# Entrada de dados do jogador:
jogador = int(input('Digite: 1 para PEDRA;\n2 para PAPEL\n3 para TESOURA:\n\n'))

# Geração de número aleatório da máquina:
pc = random.randint(1,3)
#print(pc)

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('Ainda pensando...')
time.sleep(3)

if jogador == pc:
    print('Empate')
elif (jogador == 2 and pc == 2) or (jogador == 3 and pc == 2) or (jogador == 1 and pc == 3):
    print('Jogador venceu')
else:
    print('PC venceu')






