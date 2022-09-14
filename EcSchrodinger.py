#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:48:26 2021

@author: fernando
"""

from pylab import *

MAX = 500
N = 500
m = 1.0
ht = 0.004
c = 2*m/ht
a = 1.0
INFTY = 10.*a
I = linspace(-INFTY, INFTY, N)
h = I[1]-I[0]
V0 = 20.
Eizq = -20.
Eder = -19.
epsilon = 1e-4
x_m = 1.1*a

def V(x,V0):
    if x >= -a and x <= a:
        return -V0
    else:
        return 0

def EDO(x,Y,E):
    kappa = sqrt(-2.0*m*E/ht**2)
    f0 = Y[1]
    f1 = (kappa**2 + c*V(x,V0))*Y[0]
    return array([f0, f1])

def rk4Algor(x,h,Y,f,E):
    k1 = h*f(x,Y,E)                             
    k2 = h*f(x+h/2.,Y+k1/2.,E)
    k3 = h*f(x+h/2.,Y+k2/2.,E)
    k4 = h*f(x+h,Y+k3,E)
    Z=Y+(k1 +2.*(k2+k3)+k4)/6.
    return Z

def log_dev(E,f):
    Y = zeros((2,1), float)
    kappa = sqrt(-2.0*m*E/ht**2)
    Y[0] = exp(-kappa*(-x_m))
    Y[1] = Y[0]*kappa
    
    i = 0
    while I[i] <= x_m:
        Y = rk4Algor(I[i], h, Y, f, E)
        i += 1
    
    quoLeft = Y[1]/Y[0]
    
    Y[0] = exp(-kappa*(x_m))
    Y[1] = Y[0]*kappa
    
    i = len(I)-1
    while I[i] >= x_m:
        Y = rk4Algor(I[i], -h, Y, f, E)
        i -= 1
    
    quoRight = Y[1]/Y[0]
    
    return (quoLeft - quoRight)/(quoLeft - quoRight)

def getE(Eplus, Eminus,f):
    for i in range(MAX):
        E = (Eplus+Eminus)/2.0
        Delta = log_dev(E,f)
        if (Delta*log_dev(Eplus,f)) > 0:
            Eplus = E
        else:
            Eminus = E
            
        if abs(Delta) < epsilon:
            return E
            

E = getE(Eizq, Eder, EDO)
print(E)
kappa = sqrt(-2.0*m*E/ht**2)
Y = zeros((2,N), float)
Y[0][0] = exp(kappa*(-x_m))
Y[1][0] = y[0]*kappa

i = 0
while I[i] <= x_m-h:
    Y[i+1] = rk4Algor(I[i], h, Y[i], EDO, E)
    i += 1

leftFront = i-1

Y[0][N-1] = exp(-kappa*x_m)
Y[1][N-1] = y[0]*kappa
i = N-1        
while I[i] > x_m:
    Y[i-1] = rk4Algor(I[i], -h, Y[i], EDO)
    i -= 1
    
nor = Y[0][i+1]/Y[leftFront]

for i in range(leftFront):
    Y[0][i] /= nor


xlabel('x'); ylabel('psi(x)')#; title('Ajuste spline cúbico f(x) vs x')
plot(I, Y[0], '-', lw = 2, color = 'b')
grid(True)
show()












    