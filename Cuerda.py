#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:07:11 2021

@author: fernando
"""

from numpy import *
import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D

Nx = 100                            # -Número de pasos en x.
Delta_x = 0.01                      # -Tamaño del paso en x.

Nt = 250                            # -Número de pasos en el tiempo.
Delta_t = 0.01                      # -Tamaño del paso en el tiempo.
cp = Delta_x/Delta_t; c = 0.5*cp

cons = (c/cp)**2

Yc = zeros((Nx,Nt),float);

for i in range(1, Nx-1):
    x = i*Delta_x                   # Posición inicial de la cuerda.
    Yc[i,0] = sin(2*pi*x)
    
for i in range(1,Nx-1):             # Inicializando.
    Yc[i,1] = Yc[i,0] + 0.5*cons*(Yc[i+1,0] + Yc[i-1,0] - 2.0*Yc[i,0]) 
    
for i in range(2, Nt):              # -Forma de la cuerda en un intervalo de 
    for j in range(1,Nx-1):         #  [0, tf].
        Yc[j,i] = \
        2.0*Yc[j,i-1] - Yc[j,i-2] \
        + cons*(Yc[j+1,i-1] + Yc[j-1,i-1] - 2.0*Yc[j,i-1])

x = list(range(0, Nx, 2))
y = list(range(0, Nt, 10))

X, Y = meshgrid(x,y)                
Z = Yc[X,Y]
fig = pl.figure()                       # -Hacemos la gráfica.
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color = 'b')
ax.set_xlabel('Posicion')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Altura')
pl.show()
