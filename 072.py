# Pergunte quantos jogos gerar e sorteie 6 números de 1 a 60 para cada um, guardando tudo em
# uma lista composta.
# DICA random.sample(range(1,61), 6) já garante números sem repetição.


import random # Importa a biblioteca 'random', que permite gerar números aleatórios.
jogo = [] # Cria uma lista vazia que será usada para armazenar os números de cada jogo.
jogos = [] # Cria uma lista vazia que será usada para armazenar todos os jogos.

n = int(input('Quantos jogos quer? ')) # Pergunta ao usuário quantos jogos ele quer gerar e transforma a resposta em número inteiro.
for i in range(n): # Cria um loop que será executado 'n' vezes, ou seja, uma vez para cada jogo.

   for i in range(6): # Cria outro loop que será executado 6 vezes para gerar 6 números para cada jogo.

        aleatorio = random.randint(1, 60) # Gera um número inteiro aleatório entre 1 e 60.

        while aleatorio in jogo: # Verifica se o número sorteado já existe na lista 'jogo'.

            aleatorio = random.randint(1, 60) # Se o número já existir, sorteia outro número até encontrar um que ainda não esteja na lista.

        jogo.append(aleatorio) # Adiciona o número sorteado à lista 'jogo'.

    # Inserir na Lista Principal
    jogos.append(jogo[:]) # Faz uma cópia da lista 'jogo' e adiciona essa cópia à lista principal 'jogos'.

    # Limpar a lista secundária para o próximo ciclo
    jogo.clear() # Esvazia a lista 'jogo' para que ela possa ser reutilizada na criação do próximo jogo.

for i, j in enumerate(jogos): # Percorre a lista 'jogos'. 'i' recebe o índice e 'j' recebe o conteúdo de cada jogo.

    print(f'{i} - {j}') # Exibe o número do jogo e os números sorteados. O 'f' permite inserir as variáveis dentro do texto.
