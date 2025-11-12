# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 14:52:29 2025

@author: lab54
"""

n = int(input())

pai_filho = []

for i in range(n):
    pf = input().split()
    pai_filho.append(pf)
    
R = int(input())



for j in range(n):
    if pai_filho [n][0] == R:
        filhos_R.append(pai_filho[n][1])
        
quant = len(filhos_R)
print(quant)