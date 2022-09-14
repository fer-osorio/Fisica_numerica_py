#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:46:15 2021

@author: fernando
"""
from pylab import *
import numpy as np
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Definición de constantes
N = 1000  # Número de pasos
L0=1.0  # Longitud del resorte sin estirar
L=1.0   # Lomgitud inicial del resorte estirado
v0=0.0  # velocidad inicial
theta0=0.3  # ángulo inicial en radianes
omega0=0.0  # velocidad angular inicial
k=3.5       # Constante del resorte en N/m
m=0.2       # masa en kg
g=9.81      # Aceleración gravitacional en m/s**2

# Inicializamos nuestro arreglo
y=np.zeros([4])
y[0]=L    # Establecer estado inicial
y[1]=v0
y[2]=theta0
y[3]=omega0

# Generamos tiempos igualmente espaciados
tiempo=linspace(0,25,N)

# Definimos nuestro sistema de ¡CUATRO! EDO de primer oden
def resorte(y,tiempo):
    g0=y[1]
    g1=(L0+y[0])*y[3]*y[3]-(k/m)*y[0]+g*np.cos(y[2])
    g2=y[3]
    g3=-(g*np.sin(y[2])+2.0*y[1]*y[3])/(L0+y[0])
    return array([g0,g1,g2,g3])

#  Ahora calculamos!
respuesta=odeint(resorte,y,tiempo)

# Ahora graficamos
xdatos=(L0+respuesta[:,0])*sin(respuesta[:,2])
ydatos=-(L0+respuesta[:,0])*cos(respuesta[:,2])

fig, ax = subplots()
ax.set_xlim(-0.9,0.9)
ax.set_ylim(-1.95, -1.1)
curva, = ax.plot(0,0)

x_visual = list()
y_visual = list()

def cuadros_animacion(i):
    x_visual.append(xdatos[i])
    y_visual.append(ydatos[i])
    
    curva.set_xdata(x_visual)
    curva.set_ydata(y_visual)
    
    return curva,

n = len(xdatos)    
animacion = FuncAnimation(fig, func = cuadros_animacion, \
                          frames = range(n), interval = 0.1)

"""
plot(xdatos,ydatos,'b-')
xlabel('Posición horizontal')
ylabel('Posición vertical')
"""
show()