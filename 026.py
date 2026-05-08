"""
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

"""
#Entrada de dados:
numero = int(input('Digite um número: '))
resultado = 1

while numero != 1:
    resultado = resultado * numero
    numero = numero - 1
print(f'O fatorial é: {resultado}')





