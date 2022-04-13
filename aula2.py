# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Olá, Mundo!

print("Olá, mundo!")
print("Esse é o grupo de estudos de Python")
# Variáveis simples
nome = "Álvaro"
idade = 33
temperatura = 36.5; 
tem_gatos = True
x,y = 1,2
# endereco = input("Qual é seu endereço? ")


# Estruturas de dados
## Listas
nomes = ["Álvaro","Tiago","Rafael"]
print(nomes)
print(nomes[0])
print(nomes[1])
print(nomes[2])
nomes[2] = "Xerxes"
print(nomes[2])
print(nomes)

## Dicionários
aluno = {"nome":"Álvaro",
         "curso":"Letras","RA":101}

print(aluno)
print(aluno["nome"])
print(aluno["curso"])
print(aluno["RA"])

# Controle de fluxo
# Para cada
nomes = ["Álvaro","Tiago","Rafael"]
for nome in nomes:
    print(nome)
    print("Dentro do bloco")
print("Fora do bloco")


# Funções

def somar_numeros(a,b):
    """
    Soma dois números.
    Argumentos:
        a: primeiro número
        b: segundo número
    """
    return a + b

total = somar_numeros(13029,1309)
print(somar_numeros(100,321))

help(somar_numeros)

# Módulos
print(__name__)

def main():
    pass




















