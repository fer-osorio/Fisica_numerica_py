#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:35:21 2021

@author: fernando
"""

m = 1.0; M = 1.0
aux_m = m; aux_M = M

while aux_m > 0.0:
    m = aux_m
    aux_m = aux_m/2.0
    
print("El valor mínimo (por un factor de dos) que puede ser \
representado en esta computadora es m = ", m)
print("m/2 = ", aux_m, "\n")
    
while aux_M < 1e400: #np.inf:
    M = aux_M
    aux_M = 2.0*aux_M
    
print("El valor máximo (por un factor de dos) que puede ser \
representado en esta computadora es M = ", M)
print("M*2 = ", aux_M)