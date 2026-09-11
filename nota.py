# ============================================================
# OPERAÇÕES MATEMÁTICAS
# ============================================================

# MATEMÁTICA | RESUMO

+       # soma
-       # subtração
*       # multiplicação
**      # potência
/       # divisão normal
//      # divisão inteira
%       # resto da divisão


# STRING

len()       # quantidade de caracteres
count()     # quantidade de ocorrências
find()      # primeira ocorrência
rfind()     # última ocorrência

upper()     # MAIÚSCULAS
lower()     # minúsculas
title()     # Primeira Letra De Cada Palavra
replace()   # substitui caracteres/trechos
strip()     # remove espaços do início e do final


# FATIAMENTO

texto[0]       # um caractere específico
texto[3:8]     # do índice 3 até antes do 8
texto[3:]      # do índice 3 até o final
texto[:3]      # do início até antes do 3
texto[:]       # texto inteiro


# OPERAÇÕES MATEMÁTICAS

# + → Soma
print(1 + 3)
# Resultado: 4


# - → Subtração
print(8 - 8)
# Resultado: 0


# * → Multiplicação
print(9 * 98)
# Resultado: 882


# ** → Potenciação
# 9 ** 3 significa: 9³
# Ou seja: 9 × 9 × 9
print(9 ** 3)
# Resultado: 729


# % → Resto da divisão inteira
# 81 dividido por 2 = 40, com resto 1
print(81 % 2)
# Resultado: 1
#
# O operador % é muito utilizado, por exemplo,
# para verificar se um número é par ou ímpar.
#
# Se numero % 2 == 0 → número PAR
# Se numero % 2 != 0 → número ÍMPAR


# // → Divisão inteira
# Retorna somente a parte inteira do resultado da divisão.
print(81 // 2)
# Resultado: 40
#
# A divisão normal seria:
# 81 / 2 = 40.5
#
# Com //:
# 81 // 2 = 40


# ============================================================
# STRINGS
# ============================================================

# String é uma sequência de caracteres.
# Pode conter letras, números, espaços e símbolos.
#
# As strings são colocadas entre aspas simples ou duplas.

senai = 'Luis Eulálio'


# ============================================================
# FATIAMENTO (SLICING)
# ============================================================

# Cada caractere de uma string possui uma posição (índice).
#
# A contagem começa em 0:
#
# L  u  i  s     E  u  l  á  l  i  o
# 0  1  2  3  4  5  6  7  8  9 10 11


# Acessando apenas um caractere pelo índice
print(senai[0])
# Resultado: L
#
# [0] significa: "pegue o caractere que está na posição 0"


# Fatiamento [início:fim]
print(senai[3:8])
# Pega do índice 3 até ANTES do índice 8.
#
# Índices utilizados:
# 3 → s
# 4 → espaço
# 5 → E
# 6 → u
# 7 → l
#
# Resultado: "s Eul"


# Do índice 3 até o final
print(senai[3:])
# Quando não colocamos o final, o Python entende:
# "comece no índice 3 e vá até o final."
#
# Resultado: "s Eulálio"


# Do início até antes do índice 3
print(senai[:3])
# Quando não colocamos o início, o Python começa no índice 0.
#
# Resultado: "Lui"


# String completa
print(senai[:])
# Sem início e sem fim, retorna toda a string.
#
# Resultado: "Luis Eulálio"


# ============================================================
# ANÁLISE DE STRINGS
# ============================================================

# len() → retorna a quantidade de caracteres da string.
print(len(senai))
# Conta letras, espaços e outros caracteres.
#
# Neste caso:
# "Luis Eulálio" possui 12 caracteres.


# count() → conta quantas vezes determinado caractere
# ou trecho aparece na string.
print(senai.count('l'))
# Resultado: 2
#
# O Python diferencia letras maiúsculas de minúsculas.
# Portanto, 'l' e 'L' são considerados caracteres diferentes.


# find() → procura um caractere ou trecho
# e retorna a posição da PRIMEIRA ocorrência encontrada.
print(senai.find('i'))
# Resultado: 2
#
# O primeiro "i" está no índice 2.


# rfind() → procura da direita para a esquerda
# e retorna a posição da ÚLTIMA ocorrência encontrada.
print(senai.rfind('i'))
# Resultado: 10
#
# O último "i" está no índice 10.


# ============================================================
# TRANSFORMAÇÃO DE STRINGS
# ============================================================

# upper() → transforma todas as letras em MAIÚSCULAS.
print(senai.upper())
# Resultado: "LUIS EULÁLIO"


# lower() → transforma todas as letras em minúsculas.
print(senai.lower())
# Resultado: "luis eulálio"


# title() → coloca a primeira letra de cada palavra em maiúscula.
print(senai.title())
# Resultado: "Luis Eulálio"


# replace() → substitui um caractere ou trecho por outro.
print(senai.replace('i', 'o'))
# Troca todas as ocorrências de "i" por "o".
#
# Resultado: "Luis Eulálio" → "Luos Eulálio"


# ============================================================
# STRIP
# ============================================================

# strip() → remove espaços em branco do INÍCIO e do FINAL
# de uma string.
#
# É muito utilizado quando recebemos informações do usuário
# através do input(), pois o usuário pode digitar espaços
# antes ou depois da informação.

nome = input('Digite seu nome: ').strip()

print(nome)

# Exemplo:
#
# Se o usuário digitar:
# "   Danieli   "
#
# Sem strip():
# "   Danieli   "
#
# Com strip():
# "Danieli"
#
# IMPORTANTE:
# strip() não remove os espaços ENTRE as palavras.
#
# "Danieli Silva" continua sendo:
# "Danieli Silva"

#Estrutura

#string [] - fatiamento index
#tuplas ()
#listas frutas = ['banana', 'morango', 'ameixa']
#frutas[0] = 'banana'

#dicionario JSON

# aluno = {'nome': 'Luis Tatin'}
# aluno ['nome']

# ==========================================
# CONDICIONAIS
# ==========================================

# Pede a altura ao usuário.
# float() transforma o que foi digitado em um número decimal.
altura = float(input('Altura: '))

# Verifica se a altura é maior que 1.2 metros.
if altura > 1.2:
    # Se a condição for verdadeira, executa este bloco.
    print('Pode andar no brinquedo!')

else:
    # Se a condição for falsa, executa este bloco.
    print('Quem sabe ano que vem?')


# ==========================================
# APLICANDO A LÓGICA E (AND)
# ==========================================

# Pede novamente a altura.
altura = float(input('Altura: '))

# Pede o peso.
peso = float(input('Peso: '))

# O "and" significa que AS DUAS condições precisam ser verdadeiras:
#
# 1. altura precisa ser maior que 1.2
# E
# 2. peso precisa ser menor que 200
#
# Se as duas forem verdadeiras, entra no if.
if altura > 1.2 and peso < 200:
    print('Pode ir no brinquedo')

else:
    # Se pelo menos uma das condições for falsa,
    # executa o bloco do else.
    print('Quem sabe ano que vem?')


# ==========================================
# ESTRUTURA DE REPETIÇÃO
# ==========================================

# ------------------------------------------
# 1
# ------------------------------------------

# for é utilizado para repetir um determinado bloco de código.
#
# range(1, 100) cria uma sequência começando em 1
# e terminando antes de 100.
#
# Portanto, os valores serão:
# 1, 2, 3, 4, ..., 98, 99
#
# O número 100 NÃO faz parte da sequência.
for i in range(1, 100):

    # Para cada repetição, imprime um "*".
    print('*')


# ------------------------------------------
# 2
# ------------------------------------------

# Neste caso, também começamos em 1
# e vamos até 99.
for i in range(1, 100):

    # Agora, em vez de imprimir "*",
    # imprimimos o valor armazenado na variável i.
    print(i)


# ------------------------------------------
# 3
# ------------------------------------------

# range() pode receber três valores:
#
# range(início, fim, passo)
#
# Começa em 100.
# Vai até ANTES do 1.
# O passo é -1, então estamos diminuindo 1 a cada repetição.
#
# Resultado:
# 100, 99, 98, 97, ..., 3, 2
#
# O número 1 não é incluído.
for i in range(100, 1, -1):

    # Imprime o valor atual de i.
    print(i)


# ------------------------------------------
# 4
# ------------------------------------------

# Criamos uma variável chamada soma
# e começamos seu valor em zero.
soma = 0

# O loop será executado 4 vezes:
#
# i = 1
# i = 2
# i = 3
# i = 4
#
# O 5 não entra porque o final do range não é incluído.
for i in range(1, 5):

    # Pede um número ao usuário.
    # int() transforma o valor digitado em número inteiro.
    n = int(input('Digite um número: '))

    # Adiciona o número digitado à variável soma.
    #
    # É a mesma coisa que:
    # soma = soma + n
    soma = soma + n


# Depois que o loop termina,
# temos a soma dos 4 números digitados.
#
# Dividimos a soma por 4 para calcular a média.
#
# O f-string permite colocar o resultado
# diretamente dentro do texto.
print(f'A média é {soma / 4}')


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

#Tratameto de Erro

try:
    n = int(input('Digite um número: '))
    x = 10/0
except ZeroDivisionError:
    print('Não podemos dividir por 0')
except ValueError:
    print('Só aceitamos números')

# Funções
# Uma função é um bloco de código criado para executar uma tarefa específica.
# Ela pode receber informações (parâmetros) e também pode retornar um resultado.

def quebra_linha():
    # Esta função não recebe nenhum parâmetro.
    # Quando chamada, simplesmente imprime uma linha de asteriscos.
    print("***************")


quebra_linha()
# Para executar a função, basta chamá-la pelo nome seguido de ().

def mensagem(x):
# A função mensagem recebe um parâmetro chamado x.
 # O valor passado para x será utilizado dentro da função.

quebra_linha()
# Aqui chamamos outra função que já criamos.
# Isso evita repetir o código que imprime os asteriscos.

print(x)
# Mostra na tela o conteúdo recebido pelo parâmetro x.

quebra_linha()
# Chama novamente a função quebra_linha().

mensagem("Bem vindo ao Senai")

# ***************
# Bem vindo ao Senai
# ***************

def area(x, y):
    # A função area recebe dois parâmetros: x e y.
    # Neste exemplo, eles representam as medidas de uma área.

    return x * y
    # return devolve o resultado da função.
    # Diferente do print(), o return permite guardar ou utilizar
    # esse resultado em outra parte do programa.


print(area(10,5))
# Aqui chamamos a função area() passando 10 para x e 5 para y.
# A função calcula:
# 10 * 5 = 50
#
# O return devolve 50 para o print(), que então mostra:
# 50


def volume(x, y, z):
    # A função volume recebe três parâmetros: x, y e z.
    # Neste exemplo, representam as três dimensões de um objeto.

    return area(x, y) * z
    # Aqui reutilizamos a função area() que já criamos.
    #
    # Primeiro:
    # area(x, y) calcula x * y
    #
    # Depois:
    # o resultado da área é multiplicado por z.
    #
    # Isso evita escrever novamente x * y e mostra como
    # uma função pode chamar outra função.


print(volume(10,5,8))
# Chamamos a função volume() passando:
# x = 10
# y = 5
# z = 8
#
# Primeiro a função calcula a área:
# 10 * 5 = 50
#
# Depois calcula o volume:
# 50 * 8 = 400
#
# Resultado:
# 400

# Tuplas
# Uma tupla é uma coleção de valores que pode armazenar de forma ordenada e imutável.
# diferentes tipos de dados.
# Os valores são colocados entre parênteses ().

carro = ('Ferrari', 'Vermelha', 2026)


# Fatiamento
# Podemos acessar os elementos da tupla utilizando índices.
# A contagem começa sempre pelo índice 0.

print(carro[1])
# Acessa o elemento que está no índice 1.
# Resultado: Vermelha


print(carro[0:2])
# Faz um fatiamento da tupla.
# Começa no índice 0 e vai até antes do índice 2.
# Resultado: ('Ferrari', 'Vermelha')


print(carro[-1])
# O índice -1 acessa o último elemento da tupla.
# Resultado: 2026



# Iteração
# Iterar significa percorrer os elementos de uma coleção,
# como uma tupla, lista ou outro objeto iterável.


# 1º exemplo de iteração

for i in carro:
    print(i)

# O "for" percorre cada elemento da tupla.
# A cada repetição, a variável "i" recebe um elemento.
#
# Resultado:
# Ferrari
# Vermelha
# 2026


# 2º exemplo de iteração

for i in range(0, len(carro)):
    print(carro[i])

# len(carro) retorna a quantidade de elementos da tupla.
# Neste caso:
# len(carro) = 3
#
# range(0, 3) gera os índices:
# 0, 1 e 2
#
# A variável "i" recebe esses índices e usamos
# carro[i] para acessar cada elemento.


# 3º exemplo de iteração

print(enumerate(carro))

# enumerate() cria uma sequência de pares contendo:
# índice + valor.
#
# Porém, apenas usar print(enumerate(carro)) não mostra
# diretamente os elementos da forma que normalmente queremos.
# O enumerate() é mais útil quando utilizado junto com um for.


for pos, carac in enumerate(carro):
    print(f'{pos} - {carac}')

# enumerate(carro) fornece dois valores a cada repetição:
#
# pos  = posição/índice do elemento
# carac = valor armazenado nessa posição
#
# O resultado será:
#
# 0 - Ferrari
# 1 - Vermelha
# 2 - 2026

# Tupla com várias idades
idades = (8, 9, 22, 25, 43, 87, 65, 49)


# max() retorna o maior valor da tupla
print(max(idades))
# Resultado: 87


# min() retorna o menor valor da tupla
print(min(idades))
# Resultado: 8


# sum() soma todos os valores da tupla
print(sum(idades))
# Resultado: 308


# Calculando a média das idades
# sum(idades) → soma todos os valores
# len(idades) → quantidade de elementos
# Dividindo a soma pela quantidade, temos a média
print(sum(idades) / len(idades))
# Resultado: 38.5


# sorted() organiza os valores em ordem crescente
# Do menor para o maior
print(sorted(idades))
# Resultado: [8, 9, 22, 25, 43, 49, 65, 87]


# sorted() também pode organizar em ordem decrescente
# reverse=True faz a inversão da ordem
print(sorted(idades, reverse=True))
# Resultado: [87, 65, 49, 43, 25, 22, 9, 8]
