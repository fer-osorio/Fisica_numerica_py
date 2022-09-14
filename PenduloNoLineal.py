# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:18:34 2021

@author: 52954
"""

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import ellipk

# Definición de constantes
N=5000              # Número de pasos
tau=10.0            # Tiempo en segundos de la simulación
h=tau/float(N-1)    # Paso del tiempo
omega0 = 0.         # Velocidad angular inicial
gravedad=9.8        # Aceleración 9.8 m/s**2
l = 0.5             # Longitud del pendulo


# Generamos tiempos igualmente espaciados
tiempo=linspace(0,tau,N)

# Definimos nuestra ecuación diferencial
def EDO(tiempo,estado):
    f0=estado[1]
    f1=-gravedad/l*sin(estado[0])
    return array([f0,f1])

#Método de Rhonge-Kuta
def rk4Algor(t,h,y,f):
    k1 = h*f(t,y)                             
    k2 = h*f(t+h/2.,y+k1/2.)
    k3 = h*f(t+h/2.,y+k2/2.)
    k4 = h*f(t+h,y+k3)
    y=y+(k1+2*(k2+k3)+k4)/6.
    return y 

# -Calculamos el periodo bajo un angulo inicial theta0. 
def periodo(theta0):
    # Generamos un arreglo de Nx2 para almacenar posición y velocidad
    y=zeros([N,2])
    # tomamos los valores del estado inicial
    y[0,0]=theta0
    y[0,1]=omega0
    
    for j in range(N-1):
        y[j+1]=rk4Algor(tiempo[j],h,y[j],EDO)
    
    k = 0; flag = True
    periodos = list()
    counter = 0
    for i in range(N-1):
        if counter > 10:
            break
        if y[i][0]*y[i+1][0] <= 0.0:
            if flag:
                k = i
                flag = False
            else:
                periodos.append(2.0*h*float(i-k))
                k = i
                counter+=1
                
    periodo = 0.0
    n = len(periodos)
    for i in range(n):
        periodo += periodos[i]

    return periodo/float(n)

periodo_elliptic = lambda theta0 : 4.*sqrt(l/gravedad)*ellipk(theta0)

periodos=list()
periodos_ellip=list()
diff = list()
theta0 = list()
dt = pi/float(N/50)
for i in range(1,N//50-1):
    ti = dt*float(i)
    theta0.append(ti)
    periodos.append(periodo(ti))
    k = sin(ti/2.)
    periodos_ellip.append(periodo_elliptic(k**2))
    diff.append(abs(periodos[i-1] - periodos_ellip[i-1]))

figure(1)
plot(theta0,periodos,'-r')
xlabel('Angulo inicial')
ylabel('Periodo')
title('Método 1.')
show()

figure(2)
plot(theta0, periodos_ellip, 'b')
xlabel('Angulo inicial')
ylabel('Periodo')
title('Método 2.')
show()

figure(3)
plot(theta0, diff, 'b')
xlabel('Angulo inicial')
ylabel('Periodo')
title('|Método 1 - Método 2.|')
show()

print('Diferencia máxima = ', max(diff))
