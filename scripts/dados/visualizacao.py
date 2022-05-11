# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

dados = pd.read_csv("pokemon_data.csv")
# Análise exploratória dos dados
# print(dados.tail(10))
colunas = dados.columns
# for pokemon in dados.values:
#     print(type(pokemon))

print(dados['HP'][65:70])
print(dados.loc[65:70,'Name'])

print(dados[65:70])
print(dados.loc[65:70])

dados.loc[60:70,'Name'] = 'Alvaro'
# dados['Name'][71:75] = 'Xerxes'
selecionados = dados['Name'][71:75]
# selecionados = dados.loc[71:75,'Name']

# alvaros = dados[dados['Name'] == 'Xerxes']
# alvaros = dados[60:71]
# alvaros.to_csv("alvaros.csv")
# alvaros.to_excel("alvaros.xlsx")

# Análise de estatística descritiva

sumario = dados.describe()
print(sumario)
print(sumario['HP'])

print(f"A média do HP é {dados['HP'].mean()}")

water = dados[dados["Type 1"] == "Water"]
print(f"A média do HP Water é {water['HP'].mean()}")

agrupados = dados[['HP',
                   'Type 1']].groupby('Type 1').mean().sort_values('HP',ascending=False)

# Valores faltantes

print(dados['Type 2'].isna())

# homicidios = pd.read_csv("murder_rates.csv")

# dados_pagina = pd.read_html('https://pt.wikipedia.org/wiki/COVID-19',
#                             match='Frequência dos sintomas')

# import requests
# from bs4 import BeautifulSoup

# res = requests.get('https://pt.wikipedia.org/wiki/COVID-19')
# texto = res.text

# soup = BeautifulSoup(texto,"lxml")
# h1 = soup.findAll('div')


# for tag in soup.findAll('div'):
#  print(tag.text)
 
# Visualização de dados
## relacionamentos
# Scatter
# dados.plot.scatter(x="Attack",y="Defense")
# Bolhas
# dados.plot.scatter(x="Attack",y="Defense",
                   # s="HP",alpha=0.5)
# Comparação
# Linha
# dados[['#',"HP"]].plot(x='#',y='HP')
# Barras
# dados[100:101].plot.bar()

# Distribuição
# Histograma
# dados['HP'].plot.hist()
# dados['HP'].plot.box()

agrupados.plot.box()









