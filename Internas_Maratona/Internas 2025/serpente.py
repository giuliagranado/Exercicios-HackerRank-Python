# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 14:14:50 2025

@author: lab54
"""

q = int(input())
anos = input().split()
n = 0
for i in anos:
    if (int(i)+3)%12 == 0:
        if (int(i)-2)%7 == 0:
            n+=1
print(n)