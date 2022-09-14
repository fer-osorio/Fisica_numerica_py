#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:24:34 2021

@author: fernando
"""

from scipy.interpolate import CubicSpline
from pylab import *
import numpy as np

x = [0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0]
y = [10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]

cs = CubicSpline(x, y)              # -Creamos el ajuste.
X = np.arange(0.0, 200.0, 0.1)      # -X, Y son arreglos para graficar.
Y = cs(X)

xlabel('x'); ylabel('f(x)'); title('Ajuste spline cúbico f(x) vs x')
plot(x, y, '.', lw = 2, color = 'r')
plot(X, Y, '-', lw = 2, color = 'b')
grid(True)
show()

dcs = cs.derivative()               # -Obtenemos la derivada (por secciones)
                                    #  de nuestro spline.
maxminLocs = dcs.solve()            # -Igualamos nuestra derivada a cero 
                                    #  y obenemos raices.
print(maxminLocs)                   # -Visualizamos las raíces.
x_m = maxminLocs[2]                 # -Escojemos la raíz del máximo.
print("E_r = ", x_m)
M = cs(x_m)
x_gamma = cs.solve(M/2.0)           # -Igualamos a la mitad del máximo y
                                    #  obtenemos raíces.
print(x_gamma)
Gamma = x_gamma[1] - x_gamma[0]
print('Gamma = ', Gamma)




























