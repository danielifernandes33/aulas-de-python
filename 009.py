"""
Crie um programa que leia um nome, e mostre o primeiro e o último nome

Saída esperada:

Luis Felipe Tatin Vlatkovic
Primeiro nome: Luis
Último nome: Vlatkovic
"""

#Entrada de dados:
nome_completo = input("Digite o seu nome completo: ").strip()

#Primeiro nome
inicio_primeiro_nome = nome_completo.find(' ')
#Fatiando para encontrar primeiro nome
primeiro_nome = nome_completo [0:inicio_primeiro_nome]

#Último nome
inicio_ultimo_nome = nome_completo.rfind(' ')
#Fatiando para encontrar último nome
ultimo_nome = nome_completo[inicio_ultimo_nome + 1: ]

#Retorno dos dados:

print(f'Primeiro nome: {primeiro_nome}'
      f'\nÚltimo nome: {ultimo_nome}')





