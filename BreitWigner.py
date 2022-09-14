#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:56:31 2021

@author: fernando
"""

from pylab import *
from numpy import *
from numpy.linalg import *
import pandas as pd

# -El problema consiste en encontrar el arrleglo a = [a_1, a_2, a_3].
# -Definimos nuestra función g.
# -x es el punto de evaluación de g.
def g(a, x):
    return a[0]/((x - a[1])**2 + a[2])

# -h es un "termino comun" en nuestras funciones a minimizar.
def h(a, x, y, sc):
    return (y - g(a, x))/(((x - a[1])**2 + a[2])*sc)

# -Definimos f_1
# -Los arreglos 'x' e 'y' corresponden a los dados experimentales.
# -El arreglo sc guarda las incertidumbres.
def f1(a, x, y, sc):
    n = min(len(x), len(y), len(sc))
    
    if n == 0:
        return 0
    
    val = 0.0
    for i in range(n):
        val += h(a, x[i], y[i], sc[i])
        
    return val

# Definimos f_2
# -Los arreglos 'x' e 'y' corresponden a los dados experimentales.
# -El arreglo sc guarda las incertidumbres.
def f2(a, x, y, sc):
    n = min(len(x), len(y), len(sc))
    
    if n == 0:
        return 0
    
    val = 0.0
    for i in range(n):
        val += h(a, x[i], y[i], sc[i])*(x[i] - a[1])/\
            ((x[i] - a[1])**2 + a[2])
        
    return val

# Definimos f_3
# -Los arreglos 'x' e 'y' corresponden a los dados experimentales.
# -El arreglo sc guarda las incertidumbres.
def f3(a, x, y, sc):
    n = min(len(x), len(y), len(sc))
    
    if n == 0:
        return 0
    
    val = 0.0
    for i in range(n):
        val += h(a, x[i], y[i], sc[i])/\
            ((x[i] - a[1])**2 + a[2])
        
    return val

# -Newton-Raphson multidimencional.
# -Los arreglos 'x' e 'y' corresponden a los dados experimentales.
# -El arreglo sc guarda las incertidumbres.
# -da es un valor pequeño usado para el calculo de derivadas parciales 
#  mediante central difference.
# -epsilon el la precisión que requerimos.
def NewtonRapshon(a_0, da, x, y, sc, epsilon):
    Nmax = 1000
    a = array(a_0)
    
    Da = list()                         # -Da es un arreglo de la forma 
    for i in range(3):                  #  Da = [[da/2.0, 0.0, 0.0]
        diffa = list()                  #        [0.0, da/2.0, 0.0]
        for j in range(3):              #        [0.0, 0.0, da/2.0]]
            if j != i:                  #  Este arreglo servira para 
                diffa.append(0.0)       #  aproximar las derivadas parciales.
            else:
                diffa.append(da/2.0)
        Da.append(diffa)
    Da = array(Da)
    
    F = array([f1(a, x, y, sc), f2(a, x, y, sc), f3(a, x, y, sc)])
    
    for i in range(Nmax):               # -Evitamos ciclos infinitos.
        NormaF = max(abs(F[0]), abs(F[1]), abs(F[2]))
        
        if NormaF <= epsilon:
            return a
        
        DF = list()
        for i in range(3):
            
            # -Los siguientes 3 if's son para aproximar las derivadas 
            #  parciales correspondientes.
            dFi = list()
            if i == 0:      # -Cálculo del 'gradiente' de f1.
                for j in range(3):
                    dFi.append((f1(a + Da[j], x, y, sc)\
                                - f1(a - Da[j], x, y, sc))/da)
            if i == 1:      # -Cálculo del 'gradiente' de f2.
                for j in range(3):
                    dFi.append((f2(a + Da[j], x, y, sc)\
                                - f2(a - Da[j], x, y, sc))/da)
            if i == 2:      # -Cálculo del 'gradiente' de f3.
                for j in range(3):
                        dFi.append((f3(a + Da[j], x, y, sc)\
                                    - f3(a - Da[j], x, y, sc))/da)
            DF.append(dFi)
        
        Diff_F = array(DF)          # -Arreglo de "derivadas parciales".
        IDiff_F = inv(Diff_F)       # -Inversa.
        a -= dot(IDiff_F, F)        # -Actualizamos a = [a_1, a_2, a_3]
        
        F[0] = f1(a, x, y, sc)      # -Actualizamos nuestro vector F.
        F[1] = f2(a, x, y, sc)
        F[2] = f3(a, x, y, sc)
        
    print("No se encontro un valor con suficiente precisión.")
    return a

# -Leemos los datos del archivo ''DatosBW.txt' y los transformamos a un 
#  formato conveniente.
datos = pd.read_csv('DatosBW.txt', header = 0, delim_whitespace = True)
u = datos.iloc[:, 0]
v = datos.iloc[:, 1]
w = datos.iloc[:, 2]

x = float64(u)
y = float64(v)
sc = float64(w)
for i in range(len(sc)):
    sc[i] = sc[i]**2

#sc = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

a_0 = array([45000.0, 70.0, 700.0])             # -Semilla.

# -Cálculo de nuestras a's.
# -El ajuste es muy bueno si consideramos todas las incertidumbre iguales
#  a 1.
# -Cosas mas extrañas ocurren cuando consideramos las incertidumbres dadas.
a = NewtonRapshon(a_0, 0.0003, x, y, sc, 0.001) 

print('a_1 = ', a[0], ', a_2 = ', a[1], ', a_3 = ', a[2])
print('f_r = ', a[0], ', E_r = ', a[1], ' Gamma = ', 2.0*sqrt(a[2]))

# -Imprimimos nuestro ajuste.
X = arange(0.0, 200, 0.1)
Y = list()
for i in range(len(X)):
    Y.append(g(a, X[i]))
    
xlabel('x'); ylabel('f(x)'); title('Ajuste g(x) vs x')
plot(x, y, '.', lw = 2, color = 'r')
plot(X, Y, '-', lw = 2, color = 'b')
grid(True)
show()