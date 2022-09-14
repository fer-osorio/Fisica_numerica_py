#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:08:45 2021

@author: fernando
"""

# Generador de números aleatorios.

from pylab import *
import random as rm

# Dada una lista de numeros aleatorios con distribución uniforme en [0,1], 
# esta función obtiene el coeficiente de Kolgomorov-Smirnov.
def obten_K(lista):
    lista.sort()
    n = len(lista)
    K1 = 1.0/n - lista[0]
    for i in range(1,n):
        k = (i+1.0)/n - lista[i]
        if K1 < k:
            K1 = k
            
    K2 = lista[0]
    for i in range(1,n):
        k = lista[i] - i/n
        if K2 < k:
            K2 = k
    
    if K1 <= K2:
        return sqrt(n)*K2
    
    return sqrt(n)*K1

# Inciso (a) y (b) ----------------------------------------------------------

a = 57; c = 1; M = 256 ; x_0 = 10
num_al = list()
x_n1 = x_0; x_n2 = (a*x_0 + c)%M
num_al.append(x_n2)

while x_n2 != x_0:
    x_n1 = x_n2
    x_n2 = (a*x_n1 + c)%M
    num_al.append(x_n2)

lon_g = len(num_al)
print("\n Periodo = ", lon_g, "\n")

# Inciso (c) ----------------------------------------------------------------

lon_g -= lon_g%2

xpar = list()
ximpar = list()

for i in range(lon_g):
    if i%2 == 0:
        xpar.append(num_al[i])
    else:
        ximpar.append(num_al[i])

xlabel("x_{2i-1}"); plt.ylabel("x_{2i}"); plt.title("Par vs Impar")
plot(ximpar, xpar, '.', lw = 2, color = 'b')
grid(True)
show()

# Inciso (d) ----------------------------------------------------------------

I = range(lon_g + lon_g%2)

xlabel("x_i"); plt.ylabel("i"); plt.title("x vs i")
plot(I, num_al, '.', lw = 2, color = 'g')
grid(True)
show()

# Inciso (e) ----------------------------------------------------------------
# Prueba Kolgomorov-Smirnov 

ls = len(num_al)

for i in range(ls):
    num_al[i] /= M
    
Na = list()
for i in range(12):
    Na_fila = list()
    k = i*20
    for j in range(20):
        Na_fila.append(num_al[k + j])
    Na.append(Na_fila)

K = list()
for i in range(12):
    K.append(obten_K(Na[i]))
    
print("Hemos partido la lista de números generados por nuestro método de \
congruencias lineales en 10 partes (y hemos eliminado\
los 16 ultimos). Los coeficientes Kn son:\n ")

for i in range(10):
    print("K_20 parte ", i+1, ": ", K[i])
    
print("El coeficiente KS para la lista completa es:", obten_K(num_al))

# Inciso (f) ----------------------------------------------------------------

rn = list()
for i in range(12):
    rnfila = list()
    for j in range(20):
        rnfila.append(rm.random())
        
    rn.append(rnfila)

K = list()
for i in range(12):
    K.append(obten_K(rn[i]))
    
print("\nHemos creado 12 listas, cada una de 20 numeros provenientes de la función \
random.random. Sus\
respectivos coeficientes KS son:" )

for i in range(10):
    print("K_20[", i+1, "] = ", K[i])

RN = list()
for i in range(12):
    for j in range(20):
        RN.append(rn[i][j])

print("KS de todas las listas juntas:", obten_K(RN))















