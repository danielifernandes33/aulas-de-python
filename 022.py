"""
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos

"""
soma_idades = 0
qtd_mulheres_menor_20_anos = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''

for i in range(4):
    nome = input('Qual o seu nome? ').strip()
    idade = int(input('Qual a sua idade? '))
    sexo = input('Informe o seu sexo [M/F]: ').strip().upper()[0]

    #1
    soma_idades = soma_idades + idade # ou soma_idades += idade

    #2
    if sexo == 'M' and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade

    #3
    if sexo == 'F' and idade < 20:
        qtd_mulheres_menor_20_anos += 1

print(f'A média da idade do grupo é: {soma_idades/4}'
      f'\nO nome do homem mais velho é {nome_homem_mais_velho}'
      f'\nA quantidade de mulheres com menos de 20 anos é: {qtd_mulheres_menor_20_anos}')

