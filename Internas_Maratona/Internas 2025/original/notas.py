# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 14:21:02 2025

@author: lab54
"""

string = input()
n = 0
for i in string:
    if i == "A":
        n += 1
    if i == "a":
        n += 1
print(n)