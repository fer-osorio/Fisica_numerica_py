#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:08:53 2021

@author: fernando
"""

#Calculo de pi.

import random as rm
import math as mt

d = 0.001            # Tolerancia de la varianza muestral.
Xi = 4.0*mt.sqrt(1.0 - rm.random()**2)         # Valor de nuestra función en
                                                # un punto aleatorio.
Xmi = Xi; Xi = 4.0*mt.sqrt(1.0 - rm.random()**2)   # Media muestral en i
                                                    # pasos.
Xmi_mas1 = Xmi + (Xi - Xmi)/2.0                     # Media muestral en i+1 
                                                    # pasos.
Si = 2.0*(Xmi_mas1 - Xmi)**2                    # Varianza muestral en i+2 pasos

i = 3.0
while mt.sqrt(Si/(i-1.0)) >= d:                 # Continuamos calculando mientras
    Xi = 4.0*mt.sqrt(1.0 - rm.random()**2)     # la varianza sea mayor a la 
    Xmi = Xmi_mas1                              # tolerada.
    Xmi_mas1 = Xmi + (Xi - Xmi)/i
    Si = (1.0 - 1.0/(i-1.0))*Si + i*(Xmi_mas1 - Xmi)**2
    i += 1.0

print("Estimación de Pi: " ,Xmi_mas1)
print("Intervalo de confianza: [", Xmi_mas1 - 1.96*mt.sqrt(Si/(i-1.0)),\
", ", Xmi_mas1 + 1.96*mt.sqrt(Si/(i-1.0)), "], con confianza del 95%.\n")

