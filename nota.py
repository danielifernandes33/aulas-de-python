#Operações Matemáticas

print('Bem-vindo ao Senai')
print(1 + 3) #Soma
print(8 - 8) #Subtração
print(9 * 98) #Multiplicação
print(9 ** 3) #Potenciação
print(81 % 2) #Resto da divisão inteiro
print(81 // 2) #Resultado da divisão inteira
print(81 // 2) #Resultado da divisão inteira

#String

senai = 'Luis Eulálio'

#Fatiamento

print(senai[0])
print(senai[3:8])
print(senai[3:])
print(senai[:3])
print(senai[:])

#Análise

print(len(senai)) #retorna a quantidade de caracter de uma string
print(senai.count('l')) #frequência de um determinado caracter
print(senai.find('i')) #retorna a primeira posição do caracter
print(senai.rfind('i')) #retorna a última posição do caracter

#Transformação
print(senai.upper()) #retonar a variável com todas as letras maiúsculas
print(senai.lower()) #retonar a variável com todas as letras minusculas
print(senai.title()) #
print(senai.replace('i', 'o')) #troca uma caracter pelo outro

#Strip - espaços antes e depois

nome = input('Digite seu nome: ').strip()
print(nome)


#Estrutura

#string [] - fatiamento index
#tuplas ()
#listas frutas = ['banana', 'morango', 'ameixa']
#       frutas[0] = 'banana'

#dicionario JSON

# aluno = {'nome': 'Luis Tatin'}
# aluno ['nome']

#Condicionais

altura = float(input('Altura: '))

if altura > 1.2:
    print('Pode andar no brinquedo!')
else:
    print('Quem sabe ano que vem?')

#Aplicando a lógica E
altura = float(input('Altura: '))
peso = float(input('Peso: '))

if altura > 1.2 and peso < 200:
    print('Pode ir no brinquedo')
else:
    print('Quem sabe ano que vem?')

#Estrutura de Repetição:

#1

for i in range(1,100): # final do intervalo não esta contido
    print('*')

#2

for i in range(1,100):
    print(i)

#3

for i in range(100,1,-1): # terceira posição determina o incremento do intervalo e quando não tem nada é 1
    print(i)

#4

soma = 0
for i in range(1,5):
    n = int(input('Digite um número: '))
    soma = soma + n

print(f'A média é {soma/4}')

''''''

#While (enquanto)

#1

i = 0
while i > 5:
    print('Bem vindo ao Senai')
    i +=1

#2

resposta = 'S'

while resposta != 'N':
    print('Bem vindo ao Senai')
    resposta = input('Deseja continuar [S/N]: ').strip().upper()[0]


#while true

while True:
    resposta = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break



while True:
    menu =  int(input('1.Olá\n2.Oi\n3.Sair --> '))

    if menu == 1:
        print('Olá')
    elif menu == 2:
        print('Oi')
    elif menu == 3:
        print('Sair')
        break
    else:
        print('Opção Inválida')

