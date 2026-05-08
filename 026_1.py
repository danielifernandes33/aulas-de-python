"""
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

"""
#Entrada de dados:
numero = int(input('Digite um número: '))
i =1 # variável que vai somando cada volta do loop até chegar no valor do nuúmero
resultado = 1  # variável que armazena o resultado de cada vez que o loop reinicia

while i <= numero:
    resultado = resultado * i
    i = i + 1
print(resultado)