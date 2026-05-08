"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
"""

#Entrada de dados:
nome_completo = input('Digite o nome completo: ').strip()



#3.1

print(nome_completo.upper())
print(nome_completo.lower())
nome_comleto_sem_espaco = nome_completo.replace(' ', '')
print(len(nome_comleto_sem_espaco))
print(nome_completo[0])
print(nome_completo.find(' '))

primeiro_nome = nome_completo[0:nome_completo.find(' ')]
print(primeiro_nome)
