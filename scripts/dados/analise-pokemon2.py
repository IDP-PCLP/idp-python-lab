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

# Análise exploratória de dados
## Respondendo perguntas
# Quantos pokemons estão no conjunto?
print(dados_poke.count())
# Quantos de cada tipo?
print(dados_poke.groupby("Type 1").count())
# Quantos por geração?
print(dados_poke.groupby("Generation").count())
# Qual é o Pokemon com o maior ataque?
print(dados_poke[dados_poke["Attack"] == dados_poke["Attack"].max()])
# Qual é o com a maior defesa?
print(dados_poke[dados_poke["Defense"] == dados_poke["Defense"].max()])