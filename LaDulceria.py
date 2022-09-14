#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:37:01 2021

@author: fernando
"""

#La dulcería.

import numpy as np

def ind_min(N):
    ind = 0
    for i in range(len(N)):
        if N[i] < N[ind]:
            ind = i
    return ind
        
tiempo_total = 0
te = list([0,0])
k = list([0,0])
fila = list([0,0])
m = 0
count = 0

N = np.random.rand(480)

for n in N:
    if n < 0.4:
        m = ind_min(fila)
        if fila[m] == 0:
            te[m] += 2
            fila[m] += 1
            k[m] = count
        else:
            d = (count-k[m])%2
            te[m] += 2 + 2*(fila[m]-1) + d
            fila[m] += 1
            if d == 0:
                fila[m] -= 1
        m = (m+1)%2
        if fila[m] > 0:
            if (count - k[m])%2 == 0:
                fila[m] -= 1
    elif n < 0.7:
        for j in range(2):
            m = ind_min(fila)
            if fila[m] == 0:
                te[m] += 2
                k[m] = count
                fila[m] += 1
            else:
                d = (count-k[m])%2
                te[m] += 2 + 2*(fila[m]-1) + d
                fila[m] += 1
                if j == 0:
                    if d == 0:
                        fila[m] -= 1
            if j == 0:
                m = (m+1)%2
                if fila[m] > 0:
                    if (count - k[m])%2 == 0:
                        fila[m] -= 1
    else:
        for j in range(2):
            if fila[j] > 0:
                if (count-k[j])%2 == 0:
                    fila[j] -= 1
    count += 1

tiempo_total = te[0] + te[1]
media_t = tiempo_total/len(N)

print(media_t)















