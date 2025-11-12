# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 16:17:57 2025

@author: lab54
"""

n = int(input())

linhas = []
for i in range(n):
    operacoes= input().split()
    linhas.append(operacoes)
 
def pilhas(linhas):
    pilha = []
    pilha_pos = True
    for i in linhas:
        if i[0] == 1: #inserir
            pilha.append(i[1])
        elif i[0] == 2: #deletar
            if i[1] == pilha[len(pilha)-1]:
                pilha.pop()
            else:
                pilha_pos = False
                break
    return pilha_pos
                
def fila(linhas):
    fila = []
    fila_pos = True
    for i in linhas:
        if i[0] == 1: #inserir
            fila.append(i[1])
        elif i[0] == 2: #deletar
            if i[1] == fila[0]:
                del(fila[0])
            else:
                fila_pos = False
                break
    return fila_pos

def prio(linhas):
    prio = []
    prio_pos = True
    for i in linhas:
        if i[0] == 1: #inserir
            prio.append(i[1])
        elif i[0] == 2: #deletar
            if i[1] == max(prio):
                x = max(prio)
                prio.remove(x)
            else:
                prio_pos = False
                break
    return prio_pos
    

resultado = [pilhas(linhas),fila(linhas),prio(linhas)] 

print(resultado)
  
if resultado[0]==resultado[1]==resultado[2]==False:
    print("nenhum")
elif resultado[0]==True and resultado[1]==resultado[2]==False:
    print("pilha")
elif resultado[1]==True and resultado[0]==resultado[2]==False:
    print("fila")
elif resultado[2]==True and resultado[1]==resultado[0]==False:
    print("fila de prioridade")
else:
    print("inconclusivo") 
