# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 14:41:20 2025

@author: lab54
"""

n = int(input())

pai_filho = []

for i in range(n):
    pf = input().split()
    pai_filho.append(pf)

    
R = int(input())
h = 0
def filhos(pai_filho,R,h):
    y = 0
    filhos_R = []
    for j in pai_filho:
        if int(j[0]) == R:
            filhos_R.append(j[1])
    y = len(filhos_R)
    h += y
    print(h,filhos_R)
    if y != 0:
        for i in filhos_R:
            filhos(filhos_R,i,h)
    return n 
print(filhos(pai_filho,R,h))
    