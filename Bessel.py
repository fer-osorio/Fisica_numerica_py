#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 00:57:36 2021

@author: fernando 
"""
import math

# Estas son sólo algunas funciones útiles para imprimir.
##############################################################################
def maximo(lista):
    lon = len(lista)
    M = 0
    for i in range(lon):
        if(M < lista[i]):
            M = lista[i]
            
    return M

def maximoflot(lista):
    lon = len(lista)
    M = 0.0
    for i in range(lon):
        if(M < lista[i]):
            M = lista[i]
            
    return M


def maximo_tabla(tabla):
    lon = len(tabla)
    M = 0
    for i in range(lon):
        m = maximo(tabla[i])
        if(M < m):
            M = m
            
    return M

def consigue_lon(tabla):
    longitudes = list()
    fila = list()
    ancho = len(tabla)
    largo = len(tabla[0])
    aux = ""
    for i in range(ancho):
        for j in range(largo):
            aux = str(tabla[i][j])
            fila.append(len(aux))
        longitudes.append(fila)
        fila = list()
        
    return longitudes

def ajusta_cadena(cadena, tamano):    
    c = cadena
    lon = len(c)
    if lon > tamano:
        return None
    while lon <= tamano:
        c += ' '
        lon += 1
    return c

##############################################################################
#Inciso a.

    
# - Método "up" para el calculo de las funciones de Bessel.
# - "x" es el punto a evaluar
# - "l" es un parametro que indica cuantas funciones de Bessel 
#   se van a calcular 
# - Esta función regresa una tabla cuyas filas tienen la forma
#   [i, j_i(x)]  
def bessel_up(x, l):
    if x == 0:
        print("No se atmite el valor  x = 0.")
        return None
    
    if type(l) != type(1):
        print("No se admiten valores no enteros de l")
        return None
    
    if l < 0:
        print("No se admiten valores negativos de l")
        return None
        
    if l == 0:
        print("0    ", math.sin(x)/x)
        return None
    
    if l == 1:
        print("0    ", math.sin(x)/x)
        print("1 ", math.sin(x)/(x*x)-math.cos(x)/x)
        return None
    
    j_0 = math.sin(x)/x
    j_1 = math.sin(x)/(x*x)-math.cos(x)/x
    j_l = 3.0*j_1/x-j_0
    T = list([[0, j_0], [1, j_1], [2, j_l]])
    for i in range(l-3):
        j_0 = j_1
        j_1 = j_l
        j_l = (2.0*(i+2.0)+1.0)*j_1/x-j_0
        T.append([i+3,j_l])
    
    return T

T0 = bessel_up(0.1, 25)
T1 = bessel_up(1.0, 25)
T2 = bessel_up(10.0, 25)
longitudes = consigue_lon(T0)
M = maximo_tabla(longitudes)
for i in range(len(T0)):
    c0 = ajusta_cadena(str(T0[i][1]), M)
    c1 = ajusta_cadena(str(T1[i][1]), M)
    c2 = ajusta_cadena(str(T2[i][1]), M)
    if i < 10:
        print(i, "  ", c0, " ", c1, " ", c2)
    else:
        print(i, "  ", c0, " ", c1, " ", c2)
        
#%% --------------------------------------------------------------------------
# - Metodo "down" para calcular las funciones de Bessel.
# - "x" es el punto a evaluar
# - "l" es un parametro que indica cuantas funciones de Bessel 
#   se van a calcular. 
# - "inicial1" e "inicial2" son los dos valores iniciales arbitrarios.
# - "umbral" es la diferencia entre el último valor que se desea calcular
#   (25, por ejemplo) y la cantidad de la cual se bajará (50, por ejemplo).
# - Esta función regresa una tabla cuyas filas tienen la forma
#   [i, j_i(x)]  

def bessel_down(x, l, inicial1, inicial2, umbral):
    if x == 0:
        return None
    
    if type(l) != type(1):
        print("No se admiten valores no enteros de l")
        return None
    
    if l < 0:
        return None
        
    if l == 0:
        print("0    ", math.sin(x)/x)
        return None
    
    if umbral <= 0:
        return None
    
    if l == 1:
        print("0    ", math.sin(x)/x)
        print("1    ", math.sin(x)/(x*x)-math.cos(x)/x)
        return None
    
    T = list()
    L = l+umbral
    jl = inicial1
    jlmas1 = inicial2
    jlmenos1 = (2.0*L+1.0)*jl/x-jlmas1
    for i in range(L-1,0,-1):
        jlmas1 = jl
        jl = jlmenos1
        jlmenos1 = (2.0*i+1.0)*jl/x-jlmas1
        if i <= l:
            T.insert(0, [i-1, jlmenos1])
    
    factor = (math.sin(x)/x)/T[0][1]
    for i in range(l):
        T[i][1] *= factor
    
#    for i in range(l):
#        print(T[i])
    return T

T0 = bessel_down(0.1, 25, 1.0, 2.0, 10)
T1 = bessel_down(1.0, 25, 1.0, 2.0, 10)
T2 = bessel_down(10.0, 25,1.0, 2.0, 10)
longitudes = consigue_lon(T0)
M = maximo_tabla(longitudes)
for i in range(len(T0)):
    c0 = ajusta_cadena(str(T0[i][1]), M)
    c1 = ajusta_cadena(str(T1[i][1]), M)
    c2 = ajusta_cadena(str(T2[i][1]), M)
    if i < 10:
        print(i, "  ", c0, " ", c1, " ", c2)
    else:
        print(i, "  ", c0, " ", c1, " ", c2)
        

#%% --------------------------------------------------------------------------
#Inciso b.


#Para todo i en {0, ..., L-1}, esta función encuentra un umbral "k" tal que,
#si el "down" empieza en k+L, entonces el error relativo maximo para los 
#j_i sera menor que el delta.

def bessel_down_refinado(delta, L, x):
    err_rel = 0.0
    T1 = bessel_down(x, L, 1.0, 2.0, 2)
    T2 = bessel_down(x, L, 1.0, 2.0, 3)
    ERR_REL = list()
    for i in range(L):
#        if T[i][1] == 0:
#            ERR_REL.append(0)
#        else:
        ERR_REL.append( abs( (T2[i][1] - T1[i][1])/T[i][1] ) )
    err_rel = maximoflot(ERR_REL)
    k = 1
    while err_rel > delta:
        T1 = list()
        T2 = list()
        T1 = bessel_down(x, L, 1.0, 2.0, k)
        T2 = bessel_down(x, L, 1.0, 2.0, k+1)
        ERR_REL = list()
        for i in range(L):
            ERR_REL.append( abs( (T2[i][1] - T1[i][1])/T[i][1] ) )
        err_rel = maximoflot(ERR_REL)
        k += 1
        
    Tabla = list()
    for i in range(L):
        Tabla.append([i+L, T1[i][1], T2[i][1], ERR_REL[i]])
        
    return Tabla, k

T, k = bessel_down_refinado(1e-10, 25, 1.0)
longitudes = consigue_lon(T)
M = maximo_tabla(longitudes)
for i in range(len(T)):
    c1 = ajusta_cadena(str(T[i][1]), M)
    c2 = ajusta_cadena(str(T[i][2]), M)
    c3 = ajusta_cadena(str(T[i][3]), M)
    if i < 10:
        print(i, "  ", c1, " ", c2, " ", c3)
    else:
        print(i, " ", c1, " ", c2, " ", c3)
print("\nNumero total de iteraciones:", k+1)    
print("El valor de inicio del \"down\" fue ", k+26)
#%%---------------------------------------------------------------------------
#Inciso c.


#Comparación del método "up" con el método "down".

BU = bessel_up(1.0, 50)
BD = bessel_down(1.0, 50, 1.0, 2.0, 5)

#[["l", "jl_up", "jl_down", "|jl_up-jldown|/(|jl_up|+|jl_down|)"]]
CMP = list()
for i in range(50):
    r = abs(BU[i][1] - BD[i][1])/(abs(BU[i][1]) + abs(BD[i][1]))
    CMP.append([i, BU[i][1], BD[i][1], r])

longitudes = consigue_lon(CMP)
M = maximo_tabla(longitudes)
M = len("|jl_up-jldown|/(|jl_up|+|jl_down|)")
CMP.insert(0, ["l", "jl_up", "jl_down", "|jl_up-jldown|/(|jl_up|+|jl_down|)"])
c1 = ajusta_cadena(str(CMP[0][1]), M)
c2 = ajusta_cadena(str(CMP[0][2]), M)
c3 = ajusta_cadena(str(CMP[0][3]), M)
print("l", "  ", c1, " ", c2, " ", c3)
for i in range(len(CMP)-1):
    c1 = ajusta_cadena(str(CMP[i+1][1]), M)
    c2 = ajusta_cadena(str(CMP[i+1][2]), M)
    c3 = ajusta_cadena(str(CMP[i+1][3]), M)
    if i < 10:
        print(i, "  ", c1, " ", c2, " ", c3)
    else:
        print(i, " ", c1, " ", c2, " ", c3)


   








