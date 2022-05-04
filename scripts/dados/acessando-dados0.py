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
print(dados_filmes['Carimbo de data/hora'])
print(dados_filmes['Título'])
print(dados_filmes['Categoria'])
# Executar funções de análise estatística de um DF