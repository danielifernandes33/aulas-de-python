"""
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa

"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
#operacao = int(input('Escolha uma opção:\n1.Soma\n2.Multiplicação\n3.Maior\n4.Novos números\n5. --> '))

while True:
    operacao = int(input('Escolha uma opção:\n1 - Soma\n2 - Multiplicação\n3 - Maior\n4 - Novos números\n5 - Sair do programa. --> '))

    if operacao == 1:
        print(f'Resultado da soma é: {n1 + n2 + n3}')
    elif operacao == 2:
        print(f'Resultado da multiplicação é: {n1 * n2 * n3}')
    elif operacao == 3:
        if n1>n2 and n1>n3:
            print(f'O maior número é: {n1}')
        elif n2>n3:
            print(f'O maior número é: {n2}')
        else:
            print(f'O maior número é: {n3}')
    elif operacao == 4:
        print('Digite novos números:')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        n3 = float(input('Digite o terceiro número: '))
    elif operacao == 5:
        print('Tchauzinho ;)')
        break
    else:
        print('Opção Inválida')