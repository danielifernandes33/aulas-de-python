'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

#Entrada de dados:
letra = input('Digite uma letra: ').strip().lower()[0] # o [0] faz com que o código só leia a primeira letra que o usuário digitar.

if letra in 'aeiouàáâãäéèêëíìîóòõôúùüû':
    print('Esta letra é uma vogal')
else:
    print('Esta letra é uma consoante')