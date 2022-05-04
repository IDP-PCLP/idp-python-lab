# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:37:06 2022

@author: asanorte.labdell
"""

import pandas as pd

poke_dados = pd.read_csv("pokemon_data.csv")


# Análise Exploratória dos dados
colunas = poke_dados.columns
# print(poke_dados["Name"])
# for nome in poke_dados["Name"]:
#     print(nome)

print(poke_dados["Name"][0:5])
poke_dados["Name"][0:5] = 'batata'
print(poke_dados['Name'][0:10])

print(poke_dados.loc[0:10,["#","Name"]])
print(poke_dados.iloc[0:10,0:2])

batatas = poke_dados['Name'] == 'batata'
pokemons_batatas = poke_dados[batatas]

# Quantos pokemons tem ataque maior?
maior = poke_dados['Attack'] > 150
pokemons_maior = poke_dados[maior].sort_values("Attack",ascending=False)
# Quantos pokemons tem HP maior?
maior = poke_dados['HP'] > 150
pokemons_hp_maior = poke_dados[maior].sort_values("Attack",ascending=False)

# Estatísticas descritivas
descricao = poke_dados.describe()

# poke_dados.plot()

selecao = poke_dados["Attack"]

selecao.plot(legend=True,xlabel='Numero do pokemon',
              ylabel="Ataque")
# Agrupamento

agrupado = poke_dados.groupby("Type 1").mean()

agrupado_hp = poke_dados.groupby("HP").mean()

# Valores faltantes

faltantes = poke_dados.isna()

faltantes = poke_dados[faltantes["Type 2"]]

# Webscrapping

url = 'https://pt.wikipedia.org/wiki/COVID-19'
html = pd.read_html(url,match="Frequência")



























