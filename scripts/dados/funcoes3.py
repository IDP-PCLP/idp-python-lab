#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:36:08 2022

@author: cafe
"""

import pandas as pd

arquivo = "pokemon_data.csv"

# Abrir CSV como DataFrame
dados_poke = pd.read_csv(arquivo)

# Funções de listas, dicionários e DataFrames
# Listas 
# append()	It append or add item x to the end of a list.
# insert()	Inserts the specified item x at index position i
# extend()	It adds the new to the end of an existing one.
# del	This Python list method removes the value at a specified index.
# pop()	Remove an item at a specified index and display the removed item. After removing, the remaining items moved forward to fill the index gap.
# remove()	It removes the user-specified item. It is very useful, if we know the item.
# copy()	This Python List function shallow copies the items into a new one.
# clear()	It clears the existing elements.
# count()	Counts the number of times value is repeated inside it.
# reverse()	This method reverse the items
# sort()	Sort the items in Ascending order
# index()	The index method prints the index position of a specified value.

# Dicionários
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# DataFrames
