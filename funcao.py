#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:50:31 2022

@author: mac-prof
"""

def somar_numeros(a,b):
    """
    Soma dois números.
    Argumentos:
        a: primeiro número
        b: segundo número
    """
    return a + b

print(__name__)

if __name__ == '__main__':
    
    total = somar_numeros(13029,1309)
    print(somar_numeros(100,321))
    
    help(somar_numeros)
