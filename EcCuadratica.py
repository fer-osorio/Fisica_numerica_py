#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:38:30 2021

@author: fernando
"""
import math
from tabulate import tabulate

def obten_raices(a, b, c):      
    if a == 0:                  #Evaluando casos
        if b == 0:              #particulares.
            return None
        return -c/b
    
    d = b*b-4.0*a*c
    a2 = 2.0*a
    x_1 = 0.0; x_2 = 0.0        #Raíces obtenidas con la fórmula estandar.
    y_1 = 0.0; y_2 = 0.0        #Raíces obtenidas con la segunda fórmula.
    r = []
    den1 = 0.0; den2 = 0.0
    
    if d < 0.0:                 #La ecuación tiene soluciones complejas.
        re = -(b/a2)
        d = -d
        im = math.sqrt(d)/a2
        im = abs(im)            #r[0] es un indicador para 
                                #soluciones complejas.
        r = [True, False, str(re) + "+" + str(im) + "i","--", str(re) + "-" + str(im) + "i", "--"]
        return r        
    else:                       #Calculando las raíces con la
        rd = math.sqrt(d)       #primera formula.
        c2 = 2.0*c
        x_1 = (rd-b)/a2         
        x_2 = (-b-rd)/a2        
        if c == 0:              #La segunda ecuación no se puede 
                                #útilizar con c = 0.
                                #r[1] indica cuando no se puede útilizar
                                #la segunda ecuación.
            r = [False, True, x_1, "0", x_2, "--"]
            return r
        else:                   #Evaluando la segunda formula.
            den1 = b+rd; den2 = b-rd
            if den1 == 0.0:     #Nos protejemos de alguna división entre 0                                
                y_2 = -c2/den2
                r = [False, False, x_1, "--", x_2, y_2]
                return r
            if den2 == 0.0:     #Nos protejemos de alguna división entre 0
                y_1 = -c2/den1
                r = [False, False, x_1, y_1, x_2, "--"]
                return r
            y_1 = -c2/den1     
            y_2 = -c2/den2     
            r = [False, False, x_1, y_1, x_2, y_2]
            return r
        
#Calculamos las raices de ec. con a = 1, b = 1 y c = 10^{-n},
#n = 1,2,....
            
T = list([["x_1", "y_1", "x_2", "y_2"]])
c = 1.0
raiz1 = 1.0; raiz2 = 1.0
while raiz1 != 0 and raiz2 != 0:
    T.append(obten_raices(1.0, 1.0, c))
    l = len(T)
    (T[l-1]).pop(0); (T[l-1]).pop(0)
    raiz1 = T[l-1][0]
    raiz2 = T[l-1][2]
    c /= 10.0
    
print(tabulate(T))