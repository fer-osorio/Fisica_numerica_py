#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:17:51 2021

@author: fernando
"""

# Inciso b. -------------------------------------------------------------------
from numpy import *
import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D

# -Para la solución analítica, esta función nos permite obtner el k-ésimo
#  termino de la serie que constituye a la solución.
def k_term(kappa, k, x, t):
    c = (2.0*k-1.0)*pi
    return 400.0/c*exp(-kappa*c**2*t)*sin(c*x)

# -T_analítica nos devuelve la solución analítica evaluada en un punto (x,t)
# -con la 'presicion' requerida.
def T_analitica(kappa, t, x, precision):
    T = k_term(kappa, 1.0, x, t)
    suma = T; T = k_term(kappa, 2.0, x, t)
    
    cota = 2000.0           # -Conta que nos resguarda de ciclos infinitos.
    
    k = 3.0
    while abs(T/suma) > precision:      
        suma += T
        T = k_term(kappa, k, x, t)
        k += 1.0
        if k > cota:
            break
        
    return suma


K=239.0 ; C=900.0 ; rho=2700.0      

Nx = 100                            # -Número de pasos en x.
Delta_x = 0.01                      # -Tamaño del paso en x.
Nt = 12000                           # -Número de pasos en el tiempo.
Delta_t = 0.1                       # -Tamaño del paso en el tiempo.

kappa = K/(C*rho)
etta = K/(C*rho)*Delta_t/Delta_x**2; print(etta)


T = zeros((Nx,Nt),float)

for i in range(1, Nx-1):            # Inicializando.
    T[i,0] = 100.0                  
    
for i in range(1, Nt):              # Temperatura en un intervalo de [0, tf].
    for j in range(1,Nx-1):
        T[j,i] = T[j,i-1] + etta*(T[j+1,i-1] + T[j-1,i-1] - 2.0*T[j,i-1])

x = list(range(1, Nx, 2))
y = list(range(0, Nt, 10))

X, Y = meshgrid(x,y)                
Z1 = T[X,Y]
fig = pl.figure()                    # -Hacemos la gráfica para la solución 
ax = Axes3D(fig)                     #  numérica.
ax.plot_wireframe(X, Y, Z1, color = 'b')
ax.set_xlabel('Posicion')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Temperatura')
pl.show()

#%% Inciso g. ----------------------------------------------------------------

Ta = zeros((Nx,Nt),float)           # -Iniciamos la creacion de la grafica
                                    #  de soluciones analíticas.
for i in range(0, Nt, 10):              
    for j in range(1, Nx, 2):
        Ta[j,i] = T_analitica(kappa, i*Delta_t, j*Delta_x, 0.00001)

Z2 = Ta[X,Y]
fig = pl.figure()                   # -Hacemos la gráfica.
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z2, color = 'b')
ax.set_xlabel('Posicion')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Temperatura')
pl.show()

T_diff = zeros((Nx,Nt),float)       # -Comparamos la solución analítica
                                    #  con la solución numérica mediante 
for i in range(1, Nx, 2):           #  su diferencia.
    for j in range(0, Nt, 10):
        T_diff[i,j] = T[i,j] - Ta[i, j]

Z3 = T_diff[X,Y]
fig = pl.figure()                       # -Grafica de la diferencia entre la 
ax = Axes3D(fig)                        #  solución analítica y la numérica.
ax.plot_wireframe(X, Y, Z3, color = 'b')
ax.set_xlabel('Posicion')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Temperatura')
pl.show()







