#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:36:08 2022

@author: cafe
"""

import pandas as pd

arquivo = "Filme favorito.csv"

# Abrir CSV como DataFrame
dados_filmes = pd.read_csv(arquivo)
# Acessar colunas de um DF
# Executar funções de análise estatística de um DF
titulos = dados_filmes['Título']
df_categorias = dados_filmes["Categoria"]
categorias = {}
for item in df_categorias:
    for categoria in item.split(sep=";"):
        if categoria not in categorias:
            categorias[categoria] = 1
        else:
            categorias[categoria] += 1