'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²

Saída esperada:

Volume da Esfera: Y
Área da esfera: X
'''

#Entrada de dados:

raio = float(input("Digite o raio da esfera: "))

#Cálculos
volume = (4/3) * 3.141542 * raio ** 3
area = 4 * 3.141542 * raio ** 2

#Saída

print(f'O volume da esfera é: {round(volume,2)}\nE a área é: {area:.2f}')