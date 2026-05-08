"""
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

"""
n = int(input('Digite um número: '))
i = 1 # variável que vai somando cada volta do loop até chegar no valor do nuúmero
resultado = 1  # variável que armazena o resultado de cada vez que o loop reinicia


for i in range(1, n + 1):
   resultado = resultado * i

print(f'O fatorial de {n} é {resultado}')
   