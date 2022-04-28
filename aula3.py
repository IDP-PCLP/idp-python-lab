# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Funções
def somar_numeros(a,b):
    return a+b

def main():
    nome = "Álvaro"
    idade = 33
    temperatura = 36.123456
    tem_gatos = True
    
    # Listas
    nomes = ["Gabriel","João","Pedro","xerxes","alvaro","Alvaro"]
    print(nomes)
    print(nomes[2]) # selecionando um elemento da lista
    nomes[2] = "Xerxes"
    print(nomes[2]) # selecionando um elemento da lista
     
    print(f"Eu sou amigo do {nomes[0]} fazem {idade} anos")
    print( f'{temperatura:.2f}')
    
    # Dicionários
    info = 10
    alunos = [{"nome":"Xerxes","RA":100,"curso":"Eco","info":info},
              {"nome":"álvaro","RA":101,"curso":"Jor","info":info},
              {"nome":"Alvaro","RA":101,"curso":"Jor","info":info},
              {"nome":"alvaro","RA":101,"curso":"Jor","info":info},
              {"nome":"xerxes","RA":101,"curso":"Jor","info":info}]
    print(alunos)
    print(alunos[0]["nome"])
    print(alunos[0]["RA"])
    print(alunos[0]["curso"])
    print(alunos[0]["info"])
    
    print(alunos[1]["nome"])
    print(alunos[1]["RA"])
    print(alunos[1]["curso"])
    print(alunos[1]["info"])
    
    # continuar = True
    # while continuar:
    
    #     alunos.append({})
    
    #     indice = len(alunos)-1
    #     alunos[indice]["nome"] = input("Nome: ")
    #     alunos[indice]["RA"] = input("RA: ")
    #     alunos[indice]["curso"] = input("Curso: ")
    #     alunos[indice]["info"] = input("Info: ")
    #     continuar = input("Continuar (s/n)? ")
    #     if continuar == "s":
    #         continuar = True
    #     else:
    #         continuar = False
    
    print()
    for nome in nomes:
        print(nome)
    
    nomes = []
    for aluno in alunos:
        nomes.append(aluno["nome"])
    print(sorted(nomes))
    
    for aluno in alunos:
        print("Dentro do laço")  
        if aluno["nome"].upper() == "xerxes".upper():
            print("Oi, Xerxes!")
        else:
            print("Olá, amigo")
    print("Fora do laço")
    
    
    
    print(somar_numeros(1, 2))
    print(somar_numeros("1","2"))
    
    soma = somar_numeros(1, 14334)

if __name__ == '__main__':
    main()

print()
print(__name__)







