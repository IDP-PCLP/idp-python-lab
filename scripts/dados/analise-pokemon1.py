#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:36:08 2022

@author: cafe
"""

import pandas as pd

arquivo = "pokemon_data.csv"
arquivo_xls = "pokemon_data.xlsx"
arquivo_txt = "pokemon_data.txt"

# Abrir CSV como DataFrame
dados_poke = pd.read_csv(arquivo)
# Abrir uma tabela como DataFrame
dados_poke_xls = pd.read_excel(arquivo_xls)
# Abrir TXT como DataFrame
dados_poke_txt = pd.read_csv(arquivo_txt,sep="\t")

# Análise exploratória de dados
## Determinar os nomes das colunas, número de colunas, elementos e seus tipos
print(dados_poke.head())
print(dados_poke.shape)
print(dados_poke.dtypes)

## Indexação de DataFrames
## Indexando pelo nome da coluna e número da linha
print(dados_poke['Name'][0])
for coluna in dados_poke:
    print(coluna)
for pokemon in dados_poke.values:
    print(pokemon)
for dado in pokemon:
    print(dado)
print(dados_poke.loc[dados_poke['Type 1'] == "Grass"])
## Indexando com iloc e alterando dados de um DataFrame
# dados_poke.iloc[0,0] = 1000
## Slices ou fatiar
dados_poke.iloc[:,0] = 1000
dados_poke.iloc[0,:] = 1000
dados_poke.iloc[0,1:5] = 100
## Análise exploratória
## Aplicando funções a um DataFrame
# .describe()
# .count()
# .sum()
# .mean()
# .median()
# .mode()
# .std()
# .min()
# .max()
# .abs()
# .prod()
# .cumsum()
# .cumprod()

## Agrupamento
print(dados_poke[['Attack','Type 1']].groupby('Type 1').describe())
print(dados_poke[['Attack','Type 1']].groupby('Attack').describe())
