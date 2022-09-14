#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:27:49 2021

@author: fernando
"""
import math

Tabla = list([['N', 'Suma', '|(Suma-sin(x))/sin(x)|']])

x = float(input("Introdusca el valor de x: "))

if x > 2*math.pi:
    n = 1.0
    while 2*n*math.pi <= x:
        n += 1
    x -= 2*(n-1)*math.pi

suma = x
err_rel = abs((suma-math.sin(x))/math.sin(x))
Tabla.append([1.0, suma, err_rel])
a_n = -(x**3/6.0)
n = 3.0; N = 2.0

while abs(a_n/suma) > 1.0e-16:
    suma += a_n
    err_rel = abs((suma-math.sin(x))/math.sin(x))
    N = n-1
    Tabla.append([N, suma, err_rel])
    a_n *= -(x*x/((2*n-2)*(2*n-1)))
    n += 1.0

suma += a_n; n -= 1
err_rel = abs((suma-math.sin(x))/math.sin(x))
Tabla.append([n, suma, err_rel])

for i in range(len(Tabla)):
    print(Tabla[i])