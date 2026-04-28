'''
Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

Saída esperada:

O salário de 6000 com o reajuste de 60% será de : 9600
'''

#Entrada de dados:

salario = float(input("Por gentileza, digite o seu salário: "))
reajuste = salario * 1.60

print(f"O salário de R${salario:.2f} com reajuste de 60% será R${reajuste:.2f} reais")

