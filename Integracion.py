#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:03:20 2021

@author: fernando
"""

#Integración
#Inciso a)

import random as rm
import math as mt

d = 0.001            # Tolerancia de la varianza muestral.
Xi = mt.sqrt((1.0 - rm.random()**2)**3)         # Valor de nuestra función en
                                                # un punto aleatorio.
Xmi = Xi; Xi = mt.sqrt((1.0 - rm.random()**2)**3)   # Media muestral en i
                                                    # pasos.
Xmi_mas1 = Xmi + (Xi - Xmi)/2.0                     # Media muestral en i+1 
                                                    # pasos.
Si = 2.0*(Xmi_mas1 - Xmi)**2                    # Varianza muestral en i+2 pasos

i = 3.0
while mt.sqrt(Si/(i-1.0)) >= d:                 # Continuamos calculando mientras
    Xi = mt.sqrt((1.0 - rm.random()**2)**3)     # la varianza sea mayor a la 
    Xmi = Xmi_mas1                              # tolerada.
    Xmi_mas1 = Xmi + (Xi - Xmi)/i
    Si = (1.0 - 1.0/(i-1.0))*Si + i*(Xmi_mas1 - Xmi)**2
    i += 1.0

print("Estimación de la integral del inciso a): " ,Xmi_mas1)
print("Intervalo de confianza: [", Xmi_mas1 - 1.96*mt.sqrt(Si/(i-1.0)),\
", ", Xmi_mas1 + 1.96*mt.sqrt(Si/(i-1.0)), "], con confianza del 95%.\n")

#%%---------------------------------------------------------------------------

#Nota: El programa puede tardar varios segundos en obtener el resultado.

d = 0.1     # Tolerancia de la varianza muestral.

# Xi es el valor de nuestra función en el punto aleatorio y. Notese que 
# este es el valor de la función despues del cambio de variable para ajustar
# la integral a una integral en [0,1].  
y = rm.random(); Xi = 4.0*mt.exp(16.0*y**2 - 12.0*y + 2.0) 
                                                 # un punto aleatorio.
Xmi = Xi                                         # Media muestral en i
                                                 # pasos, en este caso i = 1.
y = rm.random(); Xi = 4.0*mt.exp(16.0*y**2 - 12.0*y + 2.0); 
Xmi_mas1 = Xmi + (Xi - Xmi)/2.0                  # Media muestral en i+1 
                                                 # pasos.
Si = 2.0*(Xmi_mas1 - Xmi)**2                     # Varianza muestral en i+2 pasos

i = 3.0
while mt.sqrt(Si/(i-1.0)) >= d:      
    y = rm.random(); 
    Xi = 4.0*mt.exp(16.0*y**2 - 12.0*y + 2.0)
    Xmi = Xmi_mas1
    Xmi_mas1 = Xmi + (Xi - Xmi)/i
    Si = (1.0 - 1.0/(i-1.0))*Si + i*(Xmi_mas1 - Xmi)**2
    i += 1.0

print("Estimación de la integral del inciso b) : ", Xmi_mas1)
print("Intervalo de confianza: [", Xmi_mas1 - 1.96*mt.sqrt(Si/(i-1.0)),\
", ", Xmi_mas1 + 1.96*mt.sqrt(Si/(i-1.0)), "], con confianza del 95%.")






