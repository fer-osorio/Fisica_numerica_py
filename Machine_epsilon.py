#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:04:15 2021

@author: fernando
"""

epsilon = 1.0
aux_ep = epsilon

while 1.0 + aux_ep > 1.0:
    epsilon = aux_ep
    aux_ep = aux_ep/2.0
    
print("El epsilon de la maquina es ≈ ", epsilon, "\n")
print("1.0 + epsilon/2 = 1 +",aux_ep, " = ", 1.0 + aux_ep)