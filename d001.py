"""
Desafio 01

Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

Saída esperada:

A posição do objeto no tempo x é de y (m)
"""

#Entrada de dados:

s0 = float(input("Informe a posição inicial do objeto (m)): "))
t = float(input("Informe o tempo (s): "))
v0 = float(input("Informe a velocidade do objeto (m/s): "))
a = float(input("Informe a aceleraçaõ do objeto (m/s2: "))

# Cálculo da função horária: s = s0 + v0*t + (a * t^2) / 2
s = s0 + (v0 * t) + (a * (t**2)) / 2

#Saída de dados

print(f"\nA posição do objeto no tempo {t} é de {s} (m)")