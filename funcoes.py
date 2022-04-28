# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:33:56 2022

@author: asanorte.labdell
"""

nome = "Xerxes"
idade = 16
temperatura = 36.5
tem_pulgas = False

nomes = ["Xerxes","Calvin"]
# print(nomes[0:2])
# print(nomes[1])
aluno = {"nome":"Calvin","idade":7,
         "tem pulgas":False}

print(aluno["tem pulgas"])
aluno["tem chulé"] = True
print(aluno)

for valor in nomes:
    print(valor)
    print("if depois elif")
    if valor == "Xerxes":
        print("Oi, Xerxes!")
    elif valor == "Xerxes":
        print("Oi de novo, Xerxes!")
    else:
        print("Olá, amigo!")
    print("if e depois if de novo")
    if valor == "Xerxes":
        print("Oi, Xerxes!")
    if valor == "Xerxes":
        print("Oi de novo, Xerxes!")
    else:
        print("Olá, amigo!")

# Funções
import random

def somar_valores(a,b):
    soma = a + b
    print(a)
    print(b)
    print(soma)
    subtracao = a - b
    print(subtracao)
    if random.randint(0,1) == 0:
        return soma
    else:
        return subtracao

minha_soma = somar_valores(1234, 678)
print(minha_soma)











