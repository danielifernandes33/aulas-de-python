#Pandas

import pandas as pd
import numpay as np
from numay.random.seed(101)
df = pd
'''
#séries
#1

etiqueta =  ['a','b', 'c']
dados = [1,2,3]

serie_1 = pd.Series(data=dados, index=etiqueta)
print(serie_1)

#2
d = {'a':10, 'b':20,'c':30}
series_2 = pd.Series(data=d)
print=(series_2)

#medalhas m Série

ser1 = pd.Series(data = [1,2,3,4],index=['EUA','Alemanha','Italia', 'Japão'])
ser2 = pd.Series(data = [4,3,2,1],index=['EUA','Alemanha','Italia', 'Japão'])

#Operações Matemáticas

ser3 = ser1 *2 + ser2

#Acesso ao Conteúdo
print(ser3)
print(ser3['EUA'])

#Referencia pelo Índice

ser4 = pd.Series(data = [4,3,2,1], index=['Japão','Alemanha','Italia', 'EUA'])
print(ser3 + ser4)

#Indice que só existe de um lado

ser5 = pd.Series(data = [1,2,3], index=['Alemanha','Italia', 'Brasil'])

'''
#Data Frame

import numpy as np
from numpy.random import randn
#Data Frame
np.random.seed(101)
df = pd.DataFrame(randn(5,4),
                    ['A', 'B', 'C', 'D', 'E'],
                        ['W', 'X', 'Y', 'Z'])

print(df)

#1 Linhas - Listas com Listas por frequência
base = [['João', 54, 'M'],
        ['Maria', 54, 'F'],
        ['Thiago', 54, 'M'],
        ['Cordélia', 54, 'F']]
df_pessoas = pd.DataFrame(data= base, columns=['Nome', 'Idade', 'Sexo'])
print(df_pessoas)

#2 Dicionários - Cada valor será uma lista com todos os registros
base_dic = {'Nome': ['João', 'Maria', 'Thiago', 'Cordélia'],
            'Idade': [50, 45, 15, 25],
            'Sexo': ['M', 'F','M', 'F']}

df_pessoas = pd.DataFrame(data=base_dic)
print(df_pessoas)




