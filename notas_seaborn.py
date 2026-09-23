import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gorjeta = sns.load_dataset('tips')
#gorjeta = pd.read_excel('xpto')
'''
#Análise Exploratória
print(gorjeta.head())
print(gorjeta.info())
print(gorjeta.describe().round(2))

#Plotagem univariada
sns.histplot(gorjeta['total_bill'],bins=30, kde=True)
plt.show()

#Rugplot - cda traço é uma observação

sns.rugplot(gorjeta['total_bill'])
plt.show()

#kde
sns.kdeplot(data=gorjeta, x='total_bill')
plt.show()

#ECDF - "Que % esta abaixo de x"
sns.ecdfplot(data=gorjeta, x='total_bill')
plt.show()


#Plotagem Comparada
sns.scatterplot(data=gorjeta, x = 'total_bill', y='tip')
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data=gorjeta)
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data=gorjeta, kind='hex')
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data=gorjeta, kind='reg')
plt.show()

#Regressão separada por categoria
sns.lmplot(data=gorjeta, x = 'total_bill', y = 'tip', hue='smoker')
plt.show()

#Gráficos comparativos para todas as variáveis numéricas
sns.pairplot(gorjeta)
plt.show()

#Plotagens categóricas
sns.barplot(x= 'sex', y = 'total_bill', data=gorjeta)
plt.show()

#Gráfico de contagem
sns.countplot(x = 'sex', data=gorjeta)
plt.show()

#Diagrama de caixa
sns.boxplot(x = 'day', y = 'total_bill', data=gorjeta)
plt.show()

sns.boxplot(x = 'day', y = 'total_bill', data=gorjeta, hue='smoker')
plt.show()

'''
#Diagrama de Violino
sns.violinplot(x = 'day', y = 'total_bill', data=gorjeta, hue='sex', split=True)
plt.show()

#Gráfico de Enxame
sns.swarmplot(x = 'day', y = 'total_bill', data=gorjeta)
plt.show()

sns.pointplot(x = 'day', y = 'total_bill', data=gorjeta)
plt.show()

voos = sns.load_dataset('flights')

#Gráfico de linha
sns.lineplot(data=voos, x = 'year', y = 'passengers', marker='o')
plt.show()

#Plotagem de matriz
vp = voos.pivot_table(index='month', columns='year', values='passengers')

#Mapa de calor
sns.heatmap(vp)
plt.show()

sns.catplot(x = 'day', y = 'total_bill', data=gorjeta, kind='bar')
plt.show()

#Mapa de Cluster
sns.clustermap(vp, standard_scale=1)
plt.show()

#Salvar figuras
sns.histplot(data=gorjeta, x = 'total_bill', bins=30)
plt.title('A conta típica fica entre 10 e 20')
plt.tight_layout()
plt.savefig('Histograma.png', dpi = 200)
plt.show()
