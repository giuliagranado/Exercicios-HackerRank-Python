# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 11:33:55 2025

@author: lab54
"""

seq = input().split(",")

for i in range(0,len(seq),4):
    if seq[i] == "1":
        pos = int(seq[i+3])
        sum1 = int(seq[i+1])
        sum2 = int(seq[i+2])
        if pos < len(seq) -1:
            if sum1 < len(seq) -1:
                if sum2 < len(seq) -1:
                    seq[pos] = int(seq[sum1]) + int(seq[sum2])
            else:
                num = -1
        else:
            if sum1 < len(seq) -1:
                if sum2 < len(seq) -1:
                    seq.append(int(seq[sum1]) + int(seq[sum2]))

    elif seq[i] == 1:
        pos = int(seq[i+3])
        sum1 = int(seq[i+1])
        sum2 = int(seq[i+2])
        if pos < len(seq) -1:
            if sum1 < len(seq) -1:
                if sum2 < len(seq) -1:
                    seq[pos] = int(seq[sum1]) + int(seq[sum2])
            else:
                num = -1
        else:
            if sum1 < len(seq) -1:
                if sum2 < len(seq) -1:
                    seq.append(int(seq[sum1]) + int(seq[sum2]))
        
    elif seq[i] == "2":
        pos = int(seq[i+3])
        sum1 = int(seq[i+1])
        sum2 = int(seq[i+2])
        if pos < len(seq) -1:
            if sum1 < len(seq) -1: 
                if sum2 < len(seq) -1:
                    seq[pos] = int(seq[sum1]) * int(seq[sum2])
            else:
                num = -1
        else:
            if sum1 < len(seq) -1:
                if sum2 < len(seq) -1:
                    seq.append(int(seq[sum1]) * int(seq[sum2]))
        
    elif seq[i] == 2:
        pos = int(seq[i+3])
        sum1 = int(seq[i+1])
        sum2 = int(seq[i+2])
        if pos < len(seq) -1:
            if sum1 < len(seq) -1: 
                if sum2 < len(seq) -1:
                    seq[pos] = int(seq[sum1]) * int(seq[sum2])
            else:
                num = -1
        else:
            if sum1 < len(seq) -1:
                if sum2 < len(seq) -1:
                    seq.append(int(seq[sum1]) * int(seq[sum2]))
        
    elif seq[i] == "99":
        break
    
    elif seq[i] == "99":
        break
    
    
    else:
        num = -1
        break
    num = seq[0]
    
print(num)