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

# Lista é uma estrutura ordenada, indexada, mutável, heterogênea e que permite valores duplicados.

carro = ['Ferrari', 'Vermelha', 2026]
# Cria uma variável chamada 'carro' que guarda uma lista com três itens: o nome do carro, a cor e o ano.

# Alteração
carro[1] = 'Amarelo' 
# Altera o item que está no índice 1 da lista. O índice 1 era 'Vermelha' e passa a ser 'Amarelo'.

# Adição
carro.insert(1, 'Gasolina') # Insere 'Gasolina' no índice 1. Os itens que já estavam a partir dessa posição são deslocados uma posição para frente.
carro.append('979 CV') # Adiciona '979 CV' no final da lista.
print(carro) # Mostra na tela a lista 'carro' depois das alterações e adições.

# Remover Informações
carro.pop(4) # Remove o item que está no índice 4 da lista.
carro.remove('Gasolina') # Procura o item 'Gasolina' na lista e remove esse item.
print(carro) # Mostra na tela a lista 'carro' depois das remoções.

# Entrada
lista_idades = [] # Cria uma lista vazia chamada 'lista_idades' que será usada para armazenar as idades digitadas.

for i in range(5): # Cria um loop que será executado 5 vezes. A variável 'i' controla as repetições.
    lista_idades.append(int(input('N: '))) # Pede um valor ao usuário, transforma o valor digitado em número inteiro e adiciona esse número ao final da lista.

print(lista_idades) # Exibe na tela a lista com todas as 5 idades informadas pelo usuário.

# Cópia de listas

a = [1, 2, 3] # Cria uma lista chamada 'a' com os valores 1, 2 e 3.

b = a[:] # Cria uma cópia da lista independente de 'a'. Os dois têm os mesmos valores, mas são listas diferentes.
b = a # Cria uma cópia dependente da lista 'a'. As duas ficam "espelhadas", apontando para a mesma lista.
b.append(4) # Adiciona o número 4 no final da lista 'b'. A lista 'a' não é alterada.

print(b) # Exibe a lista 'b': [1, 2, 3, 4].
print(a) # Exibe a lista 'a': [1, 2, 3].

#Resumo
b = a    # Cópia dependente → listas espelhadas
b = a[:] # Cópia independente → cria uma nova lista

#Lista aninhada

# Coluna
Alunos = [['Maria', 22], ['João', 53], ['Thiago', 32]] # Cria uma lista com 3 listas internas. Cada lista representa um aluno com nome e idade.

Alunos = [['Maria', 'João', 'Thiago'], [22, 53, 32]] # Organiza os dados em duas listas: a primeira guarda os nomes e a segunda guarda as idades.

Alunos = [[], []] # Cria uma lista com duas listas vazias: uma será usada para os nomes e a outra para as idades.

for i in range(3): # Cria um loop que será executado 3 vezes para cadastrar 3 alunos.
    Alunos[0].append(input('Nome: ')) # Pede o nome do aluno e adiciona o valor na primeira lista, que está no índice 0.
    Alunos[1].append(int(input('Idade: '))) # Pede a idade, transforma o valor em inteiro e adiciona na segunda lista, que está no índice 1.

print(Alunos) # Exibe na tela a lista completa com os nomes e as idades cadastradas.


# ===================== DICIONÁRIOS =====================

# O QUE É UM DICIONÁRIO EM PYTHON
#
# Um dicionário (dict) é uma estrutura de dados do Python que guarda informações em pares de chave: valor, em vez de guardar só valores soltos como numa lista.
#
# Exemplo:
# aluno = {'Nome': 'Luis Tatin', 'Idade': 45}
#
# Aqui, 'Nome' e 'Idade' são as chaves, e 'Luis Tatin' e 45 são os valores associados a elas.
#
#
# PRINCIPAIS CARACTERÍSTICAS
#
# 1) Pares chave-valor
# Cada informação é acessada através de uma chave, não de uma posição numérica como em listas.
# Ex.: aluno['Nome'] em vez de aluno[0]
#
# 2) Chaves únicas
# Não pode haver duas chaves iguais no mesmo dicionário. Se você atribuir um valor a uma chave que já existe, o valor antigo é sobrescrito.
#
# 3) Chaves devem ser "hashable" (imutáveis)
# Normalmente são strings, números ou tuplas. Não pode usar listas ou outros dicionários como chave, porque eles são mutáveis.
#
# 4) Valores podem ser qualquer coisa
# Strings, números, listas, outros dicionários, funções etc. Sem restrição.
#
# 5) Mutável
# Dá para adicionar, alterar e remover pares depois de criado:
# aluno['Sexo'] = 'M'   -> adiciona
# aluno['Idade'] = 46   -> altera
# del aluno['Sexo']     -> remove
#
# 6) Mantém a ordem de inserção
# Desde o Python 3.7, os itens são percorridos na mesma ordem em que foram adicionados (antes disso a ordem não era garantida).
#
# 7) Tamanho dinâmico
# Cresce ou diminui livremente, sem precisar definir um tamanho fixo.
#
# 8) Iterável
# Dá para percorrer chaves (.keys()), valores (.values()) ou os dois juntos (.items()).
#
# 9) Busca rápida
# Acessar um valor por chave é muito eficiente (tecnicamente O(1) na média), porque internamente o Python usa uma tabela hash. Bem mais rápido que procurar um item numa lista grande.
#
#
# RESUMO
# Dicionários são ideais quando você quer nomear cada informação (como um registro: nome, idade, sexo) em vez de só empilhar valores em sequência.


# Cria um dicionário com duas chaves: 'Nome' e 'Idade'
df = {'Nome': 'Luis Tatin', 'Idade': 45}

print(df['Nome'])   # Acessa o valor associado à chave 'Nome' e imprime na tela
df['Sexo'] = 'M'    # Cria uma NOVA chave 'Sexo' no dicionário e atribui o valor 'M'
del df['Idade']     # Remove a chave 'Idade' (e seu valor) do dicionário

# ----- Mostrar dados -----
print(df)            # Imprime o dicionário completo (todas as chaves e valores)
print(df.values())   # Imprime só os VALORES do dicionário (retorna um objeto dict_values)
print(df.keys())     # Imprime só as CHAVES do dicionário (retorna um objeto dict_keys)
print(df.items())    # Imprime os pares (chave, valor) como tuplas (objeto dict_items)

# ----- Itera os valores em sequência -----
quebra_linha()          # Chama a função externa para separar visualmente a saída
for i in df.values():   # Percorre cada VALOR do dicionário, um por vez
    print(i)              # Imprime o valor da vez (i recebe cada valor, não a chave)

# ----- Itera as chaves em sequência -----
quebra_linha()           # Separa novamente a saída no console

for i in df.keys():      # Percorre cada CHAVE do dicionário, uma por vez
    print(i)               # Imprime a chave da vez

# ----- Criação de lista auxiliar -----
chaves = [i for i in df.keys()]
# List comprehension: para cada chave (i) em df.keys(), guarda i numa nova lista.
# Equivale a: chaves = list(df.keys())
print(chaves)   # Imprime a lista de chaves criada


# ===================== 1 - LISTA COM DICIONÁRIOS =====================
# Aqui cada elemento da lista é um dicionário, representando um "carro"
df = [{'Marca': 'A', 'Modelo': 'X', 'Ano': 2000},
      {'Marca': 'B', 'Modelo': 'Y', 'Ano': 2001},
      {'Marca': 'C', 'Modelo': 'Z', 'Ano': 2002}]

for carro in df:   # Percorre a lista; a cada volta, 'carro' é um dos dicionários
    print(f'Marca : {carro["Marca"]} - Modelo: {carro["Modelo"]}')
    # Imprime a marca e o modelo do carro atual.
    # Observação: no seu código original as aspas internas eram simples,
    # iguais às da f-string (carro['Marca']). Isso só funciona em Python 3.12+;
    # em versões anteriores dá erro de sintaxe. Aqui troquei as internas para
    # aspas duplas para garantir compatibilidade com qualquer versão.

# ----- Exemplo Manual (cadastro via input) -----
df = []       # Lista vazia que vai guardar todos os dicionários de carros cadastrados
carro = {}    # Dicionário "molde", reaproveitado a cada volta do laço
try:
    for i in range(3):   # Repete o cadastro 3 vezes (i não é usado, só conta as voltas)
        carro['Marca'] = input('Marca: ')      # Lê a marca digitada e guarda no dicionário
        carro['Modelo'] = input('Modelo: ')    # Lê o modelo digitado e guarda no dicionário
        carro['Ano'] = int(input('Ano: '))     # Lê o ano digitado e converte para inteiro

        df.append(carro.copy())
        # Adiciona uma CÓPIA do dicionário 'carro' à lista df.
        # É essencial usar .copy(): sem ela, todos os itens da lista
        # apontariam para o MESMO dicionário na memória, e ao final
        # todos teriam os dados do último cadastro feito.

    print(df)   # Imprime a lista completa de carros cadastrados
except ValueError:
    # Esse erro acontece se o usuário digitar algo que não seja um
    # número válido no campo 'Ano' (int() não consegue converter)
    print('Só aceitamos números')


# ===================== 2 - DICIONÁRIO COM LISTAS =====================
# Agora a estrutura é invertida: um único dicionário onde cada chave
# guarda uma LISTA de valores (como se fossem "colunas" de uma tabela)
df = {'Marca': ['A', 'B', 'C'],
      'Modelo': ['X', 'Y', 'Z'],
      'Ano': [2000, 2001, 2002]}

# print(f'A média é {sum(df['Ano'])/len(df['Ano'])}')
# (linha deixada comentada no original) Calcularia a média dos anos:
# soma todos os valores da lista df['Ano'] e divide pela quantidade de itens

# ----- Exemplo Manual -----
df = {}   # Reinicia df como um dicionário vazio

# Input do dicionário com 1 linha
df['Marca'] = [input('Marca: ') for i in range(3)]
# List comprehension: pede 3 marcas ao usuário, uma por vez,
# e já guarda o resultado como lista na chave 'Marca'
df['Modelo'] = [input('Modelo: ') for i in range(3)]
# Mesma lógica, agora pedindo os 3 modelos
df['Ano'] = [int(input('Ano: ')) for i in range(3)]
# Mesma lógica, pedindo os 3 anos e convertendo cada um para inteiro

for i, j in df.items():   # Percorre os pares (chave, valor) do dicionário
    print(f'{i} - {j}')     # Imprime a chave (i) e a lista de valores correspondente (j)

# ----- Exemplo compatível de uma lista -----
marcas = []   # Lista vazia para guardar as marcas
for i in range(3):
    marcas.append('Digite uma Marca: ')
    # ATENÇÃO (possível bug do original): aqui está sendo adicionado o
    # TEXTO literal 'Digite uma Marca: ' na lista, e não uma marca
    # realmente digitada pelo usuário. Para capturar o que o usuário
    # digita, seria preciso usar:
    #     marcas.append(input('Digite uma Marca: '))

df['Marca'] = marcas[:]
# Substitui a lista de marcas do dicionário por uma CÓPIA da lista 'marcas'.
# O uso de [:] cria uma nova lista com os mesmos elementos, evitando que
# df['Marca'] e marcas apontem para o mesmo objeto na memória.


# ===================== EXERCÍCIO: CADASTRO DE ALUNOS =====================
# Enunciado:
# Crie um programa que leia o nome, sexo e idade de vários Alunos,
# guardando os dados de cada aluno em um dicionário e
# todos os dicionários em uma lista. No final mostre:
#   - Quantas pessoas foram cadastradas
#   - A média de idade do grupo
#   - Uma lista com todas as mulheres
#   - Uma lista com todas as pessoas com idade acima da média

# Exemplo de estrutura esperada, só para referência/estudo
# (dicionário de dicionários: chave = nome, valor = dados do aluno)
alunos = {'A': {'Idade': 45, 'Sexo': 'M'},
          'B': {'Idade': 15, 'Sexo': 'F'},
          'C': {'Idade': 35, 'Sexo': 'M'}}


# ----- Início da solução real -----
alunos = {}   # Reinicia 'alunos' como um dicionário vazio: chave = nome, valor = dados

while True:   # Laço infinito; só é interrompido pelo 'break' lá dentro
    nome = input('Nome [Sair para parar]: ').strip().title()
    # Lê o nome digitado, remove espaços extras no início/fim (strip)
    # e deixa a primeira letra de cada palavra em maiúscula (title)
    if nome == 'Sair':   # Se o usuário digitar "sair" (vira "Sair" após o .title())
        break              # Encerra o laço de cadastro

    alunos[nome] = {'Idade': int(input('Idade: ')),
                     'Sexo': input('Sexo[M/F]: ').strip().upper()[0]}
    # Cria (ou sobrescreve, se o nome já existir) a entrada do dicionário
    # 'alunos' para a chave 'nome', com um dicionário interno contendo:
    #   'Idade' -> valor digitado, convertido para inteiro
    #   'Sexo'  -> valor digitado, sem espaços, em maiúsculo,
    #              pegando só o primeiro caractere ([0])
    #              ex.: 'feminino' -> 'FEMININO' -> 'F'

# ----- Lista Mulheres -----
lista_nomes_mulheres = []   # Lista vazia para guardar os nomes das alunas
for k, v in alunos.items():
    # k = nome do aluno (chave); v = dicionário {'Idade': ..., 'Sexo': ...} (valor)
    if v['Sexo'] == 'F':                # Verifica se o sexo cadastrado é Feminino
        lista_nomes_mulheres.append(k)  # Se for, adiciona o nome à lista de mulheres

# ----- Lista Pessoas Acima da média -----
lista_nomes_acima_media = []   # Lista vazia para guardar quem está acima da média de idade
for k, v in alunos.items():
    # Recalcula a média de idade a cada volta do laço (não é o mais eficiente,
    # mas funciona): soma a idade de todos os alunos e divide pela quantidade
    if v['Idade'] > sum(aluno['Idade'] for aluno in alunos.values()) / len(alunos):
        lista_nomes_acima_media.append(k)
        # Se a idade do aluno atual for maior que a média, guarda o nome dele

quebra_linha()   # Separa visualmente a saída antes de mostrar o resumo final

print(f'Quantas pessoas foram cadastradas: {len(alunos)}'
      # len(alunos) conta quantas chaves (alunos) existem no dicionário
      f'\nA média de idade é {sum(aluno["Idade"] for aluno in alunos.values()) / len(alunos)}'
      # Soma todas as idades dos alunos e divide pela quantidade de alunos
      f'\nA lista de mulheres: {lista_nomes_mulheres}'
      # Mostra a lista com os nomes das alunas cadastradas
      f'\nA lista das pessoas com idade acima da média: {lista_nomes_acima_media}')
      # Mostra a lista com os nomes de quem tem idade acima da média



