#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:36:08 2022

@author: cafe
"""
# Abrir CSV como DataFrame (0,1 ponto)
import pandas as pd

arquivo = "pokemon_data.csv"
dados_poke = pd.read_csv(arquivo)

# Escreva na tela o nome dos 100 primeiros Pokemons (0,2 ponto).
print(dados_poke['Name'][0:100])
# Escreva na tela o nome de todos os Pokemons do tipo "Bug" e que tenham ataque maior que 50 (0,3 ponto)
# print(dados_poke[['Name','Type 1','Attack']][dados_poke['Type 1'] == 'Bug'][dados_poke['Attack'] > 50])
# Segunda forma
bugs = dados_poke[['Name','Type 1','Attack']][dados_poke['Type 1'] == 'Bug']
print(bugs[['Name','Type 1','Attack']][bugs['Attack'] > 50])
# Escreva na tela a média da velocidade ("Speed") de todos os Pokemons agrupado por tipo 1 ("Type 1") (0,3 ponto)
print(dados_poke[['Speed','Type 1']].
      groupby(['Type 1']).mean().sort_values(['Speed'],
                                             ascending=False))