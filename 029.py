'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''
from xml.dom.minidom import ProcessingInstruction

qtd_numeros = 0
soma = 0

while True:
    n = input('Digite um número: ')

    if n == '0000':
        break

    qtd_numeros += 1
    soma = soma + int(n)

print(f'A quantidade de números digitados é: {qtd_numeros}'
      f'\nA soma de todos os números é: {soma}')

