#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:00:35 2021

@author: fernando
"""

from numpy import *
import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D

Nx = 150                    # -Pasos en x.
Ny = Nx                     # -Pasos en y.

# -La constante 'k' nos asegura que el tamaño de los lados de nuestra 
#  malla sea un multiplo de 2pi.
k = 2.0 

sizeLen = 2.0*pi*k          # -Longitud de los lados de nuestro campo.
                            
MAX = 100                   # -Número máximo de ciclos.
Dx = sizeLen/float(Nx)      # -Longituds de paso.
Dy = sizeLen/float(Ny)
epsilon = 1e-6              # -Presición requerida

# -La función 'rho' juega el papel de nuestra 'f' del ejercicio.
def rho(x,y):
    return cos(3.0*x+4.0*y) - cos(5*x-2*y)

# -'f' ayudará a establecer las condiciones de frontera en el eje x.
def f(x):
    return 0#sin(x)

# -'g' ayudará a establecer las condiciones de frontera en el eje y.
def g(y):
    return 0#cos(y)

# -'Field' es un arreglo de dos dimensiones. En este caso la malla sobre la 
#  cual trabajaremos.
# -'bound_cond' establece las condiciones de frontera. Es decri, da valores 
#  a los lados de nuestra malla.
def bound_cond(Field):
    lenx = len(Field)
    leny = len(Field[0])
    dx = sizeLen/float(lenx)
    dy = sizeLen/float(leny)
    
    # -Damos valores a las esquinas.
    Field[0][0] = (f(0) + g(0))/2.0
    Field[lenx-1][0] = (f(dx*float(lenx)) + g(0))/2.0
    Field[0][leny-1] = (f(0) + g(dy*float(leny-1)))/2.0
    Field[lenx-1][leny-1] = (f(dx*float(lenx)) + g(dy*float(leny-1)))/2.0
    
    # -Asignamos valores a los lados paralelos al eje x.
    for i in range(1,lenx-1):
        Field[i][0] = f(dx*float(i))
        Field[i][lenx-1] = f(dx*float(i))
    
    # -Asignamos valores a los lados paralelos al eje y.
    for i in range(1,leny-1):
        Field[0][i] = g(dy*float(i))
        Field[leny-1][i] = g(dy*float(i))

# -Creamos nuestro campo.
Field = zeros((Nx,Ny),float)
# -Asignamos valores a la frontera.
bound_cond(Field)

counter = 0

# -Para cada punto (i,j) y para cada actualización del valor de este punto,
# 'local_diff' guarda la diferencia entre el valor viejo y el valor nuevo.
local_diff = 1.0       

# -En cada actualización de nuestro campo, 'max_diff' guarda el mayor de 
#  los 'local_diff'.
max_diff = 1.0
old_val = 0.0

# -Aplicamos el método de Gauss-Seidel.
while max_diff >= epsilon and counter < MAX:
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            x = Dx*float(i)
            y = Dy*float(j)
            
            # -Guardamos el valor viejo.
            old_val = Field[i][j]
            # -Actualizamos el punto (i,j) de nuestra malla.
            Field[i][j] = (Field[i+1][j] + Field[i-1][j] + Field[i][j+1] +\
                           Field[i][j-1])/4.0 - rho(x, y)/4.0
            # -Encontramos la distancia entre el valor viejo y el nuevo
            #  valor.
            local_diff = abs(Field[i][j] - old_val)
            # -De ser necesario, actualizamos 'max_diff'.
            if local_diff < max_diff:
                max_diff = local_diff 
            
    counter+=1
    
Del = 0.0
Delmax = 0.0

# -Imprimimos.        
nx = int(Nx/4)      # -Decidimos hasta que punto del eje x imprimiremos,
                    #  en este caso solo tomamos un cuarto de los puntos.
ny = int(Ny/4)      # -Decidimos hasta que punto del eje y imprimiremos,
                    #  en este caso solo tomamos un cuarto de los puntos.
x = list(range(nx))
y = list(range(ny))
X,Y = meshgrid(x,y)
Z = Field[X,Y]
fig = pl.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z,color='b')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('phi(x,y)')
pl.show()