#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:48:53 2021

@author: fernando
"""

from numpy import *
from numpy.linalg import*
import matplotlib.pyplot as plot

#Definimos nuestra función a ajustar.
def V(x, v_0, gamma):
    return v_0*exp(-gamma*x)
    

x = array([0.0, 32.8, 65.6, 98.4, 131.2, 164.0, 196.8, 229.6,\
     262.4, 295.2, 328.0, 360.8, 393.6, 426.4, 459.2, 492.0])
Vol = array([5.08, 3.29, 2.23, 1.48, 1.11, 0.644, 0.476, 0.273, \
       0.188, 0.141, 0.0942, 0.0768, 0.0322, 0.0322, \
           0.0198, 0.0198])
sigma = array([1.12e-01, 9.04e-02, 7.43e-02, 6.05e-02, 5.25e-02,\
         4.00e-02, 3.43e-02, 2.60e-02, 2.16e-02, 1.87e-02,\
             1.53e-02, 1.38e-02, 8.94e-03, 8.94e-03, 7.01e-03,\
                 7.01e-03])
    
y = log(Vol)            # -'Linealizamos' nuestros datos
n = len(x)
Uno = ones(n)

sigmaInv = Uno/sigma 
sx = sigmaInv*x
sy = sigmaInv*y
sxx = sx*x
sxy = sy*x


S = sum(sigmaInv)
Sx = sum(sx)
Sy = sum(sy)
Sxx = sum(sxx)
Sxy = sum(sxy)


A = array([[S, Sx], [Sx, Sxx]])
b = array([Sy, Sxy])
t = solve(A,b)

v_0 = exp(t[0]); gamma = -t[1]
print('V_0 = ', v_0,', Gamma = ' ,gamma)

Voltaje = V(x, v_0, gamma)
ChiCuadrada = sum((Vol - Voltaje)**2*sigmaInv)
print('Chi Cuadrada = ' ,ChiCuadrada)


X = arange(0.0, 492.0, 0.1)
Y = V(X, v_0, gamma)
plot.grid(True, which = 'both')
plot.semilogy(x, Vol, color = 'b', marker = '.')
plot.semilogy(X, Y, color = 'g')
plot.xlabel('Tiempo')
plot.ylabel('Voltaje')
plot.show()