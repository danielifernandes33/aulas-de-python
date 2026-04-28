'''

Escreva um programa que leia 6 notas diferentes e faça a média do aluno

Saída esperada:

A sua média final é : 5

'''

# Entrada de dados:

nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))
nota4 = float(input("Digite a nota: "))
nota5 = float(input("Digite a nota: "))
nota6 = float(input("Digite a nota: "))

#Saída de dados:

media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6

print(f"A média do aluno é: {media:.1f}")
