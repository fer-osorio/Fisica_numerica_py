#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:08:49 2021

@author: fernando
"""

import random as rm
from pylab import *


# Inciso a. -------------------------------------------------------------------

# -Función que devuelve los pasos de una caminata aleatoria. 
# -EL parametro 'N' es para la cantidad de pasos de nuestra caminata.
# -Las listas pasosX y pasosY guardan, para cada paso, los incrementos en 
#  direccion 'x' y direccion 'y' respectivamente.
def pasos(N):
    pasosX = list()
    pasosY = list()
    x = 2*rm.random() - 1; y = 2*rm.random() - 1
    L = sqrt(x**2 + y**2)
    x /= L; y /= L              # Normalizamos.
    
    pasosX.append(x); pasosY.append(y)
    # Hasta aqui solo hemos inicializado nuestras listas.
    
    for i in range(1,N):
        x = 2*rm.random() - 1; y = 2*rm.random() - 1
        L = sqrt(x**2 + y**2)
        x /= L; y /= L          # Normalizamos.
        pasosX.append(x); pasosY.append(y)
        
    return pasosX, pasosY


# -Los parametros 'pasosX' y 'pasosY' son listas que contienen los pasos
#  en dirección 'x' y dirección 'y' respectivamente.
# -(x_0, y_0) es el punto de inicio de la caminata.
def caminata(pasosX, pasosY, x_0, y_0):
    longitud = len(pasosX)
    
    x = x_0; y = y_0        #
    caminataX = list([x])   # Inicializando listas.
    caminataY = list([y])   #
    
    for i in range(longitud):
        x += pasosX[i]
        y += pasosY[i]
        caminataX.append(x)
        caminataY.append(y)
        
    return caminataX, caminataY
    

# -Función que regresa la el cuadrado de la distancia de la semilla al punto 
#  final de una caminata aleatoria.
def distfinal_cuad(caminataX, caminataY):       
    longitud = len(caminataX)
    x = caminataX[longitud - 1] - caminataX[0]
    y = caminataY[longitud - 1] - caminataY[0]
    
    return x**2 + y**2

# Inciso b y c. -------------------------------------------------------------------

N = 5000;

#------------------------------------------------------------------------------
# -Esta parte del codigo solo imprime una de las caminatas.
#pasosX, pasosY = pasos(N)

# -Los elementos de las semillas son números en los intervalos [-10, 10]
#X, Y = caminata(pasosX, pasosY, 20*rm.random() - 10, 20*rm.random() - 10)

#title('Caminata aleatoria.',)
#plot(X, Y,'-', lw = 2, color = 'b')
#grid(True)
#show()
#------------------------------------------------------------------------------

R2 = 0.0                         # -Distancia al cuadrado.
Suma_R2 = 0.0; k = int(sqrt(N))  # -Suma de los cuadrados de las distancias y 
                                 #  número de experimentos.
                                 
Suma2_pasosX = 0.0               # -Suma de los cuadrados de los incrementos.
Suma2_pasosY = 0.0               #  Esto es para el inciso d.

T = 0.0                          # -La variable T guardara la división entre
                                 #  la diferencia de el cuadrado de la 
                                 #  distancia final y la suma de los 
                                 #  cuadrados de los incrementos en los ejes 
                                 #  'x' y 'y' con el cuadrado de la 
                                 #  distancia. Esto es para en inciso d.
                                 
pasosX = list(); caminoX = list()
pasosY = list(); caminoY = list()

for i in range(k):    
    # -Puntos iniciales. Cada elemento pertenece al intervalo [-10,10]
    x_0 = 20.0*rm.random() - 10.0; y_0 = 20.0*rm.random() -10.0
    pasosX, pasosY = pasos(N)                               # -Creamos las 
    caminoX, caminoY = caminata(pasosX, pasosY, x_0, y_0)   #  caminatas.
    
    R2 = distfinal_cuad(caminoX, caminoY)   # Calculando distancia final al
                                            # al cuadrado.    
                                            
    for i in range(N):                  # -Ciclo para el inciso d.
        Suma2_pasosX += pasosX[i]**2    # -Suma del cuadrado de los 
        Suma2_pasosY += pasosY[i]**2    #  incrementos.

    T += (R2 - Suma2_pasosX - Suma2_pasosY)/(2.0*R2)
    Suma_R2 += R2
    
R2med = Suma_R2/k        # Media del cuadrado de las distancias.
print('El valor esperado para R^2(N) es aproximadamente: ', R2med)

# Inciso d. ------------------------------------------------------------------

Tmed = abs(T/k)
DxDy = Tmed/(2.0*N*(N-1.0))             # Media de la variable T en valor absoluto.
print('En promedio, el valor de (\Delta x_i\Delta x_j)/R^2 (i != j) es', DxDy)

#%% Inciso e. -------------------------------------------------------------------

# Esta parte del codigo puede tardarse algunos segundo en ejecutar.

i = 10; M = 100 # Definimos nuetra i inicial y nuestro limite superior M.
incremento = 1  # Definimos el incremento en nuestra grafica.
Rrms = list()
R = 0.0
sqrtN = list()

while i <= M:
    N = i*i         # Estableciendo número de pasos.
    
    for j in range(i):
        pasosX, pasosY = pasos(N)                               # -Creando las 
        caminoX, caminoY = caminata(pasosX, pasosY, 0.0, 0.0)   #  caminatas.
    
        # Calculando y guardando el valor cuadratico medio.
        R += sqrt(distfinal_cuad(caminoX, caminoY))
        
    Rrms.append(R/i) 
                                         
    sqrtN.append(i)    # Guardando \sqrt(N), en este caso i.                                                
    
    i += incremento         
    
    
title('Rrms vs sqrtN')                     # -Graficando el error cuadratico
xlabel('sqrtN'); ylabel('Rrms')            #  medio contra la raiz cuadrada 
plot(sqrtN, Rrms,'.', lw = 2, color = 'b') #  de el número de pasos.
grid(True)
show()
    
    
    
    
    
    
    
    
    
    
    
    
    





    