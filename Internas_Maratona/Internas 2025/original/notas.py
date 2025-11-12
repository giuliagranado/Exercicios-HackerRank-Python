# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 14:21:02 2025

@author: lab54
"""
n = int(input())

todas_notas = []

for i in range(n):
    num_notas = int(input())
    notas = input().split()
    for j in range(num_notas):
        todas_notas.append(notas[j])

ordenados = sorted(todas_notas, reverse=True)
print(ordenados)