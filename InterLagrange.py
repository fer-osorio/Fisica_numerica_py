#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:03:36 2021

@author: fernando
"""
# -Manejaremos a los polinomios como arreglos.
from pylab import *

# -Si el coeficiente principal es cero, esta función lo remueve. Repite el 
#  poceso hasta encontrar un coeficiente no cero.
def quitaCeros(P):
    p = len(P)
    
    if p == 0:
        return P
    
    while p > 0 and P[p-1] == 0.0:
        P.pop()
        p -= 1
    
# -Definimos la suma de polinomios.
def sumaPol(P, Q):
    p = len(P); q = len(Q)
    
    if p == 0:
        return Q
    
    if q == 0:
        return P
    
    R = list()
    if p > q:
        for i in range(q):
            R.append(P[i] + Q[i])
        for i in range(q, p):
            R.append(P[i])
    else:
        for i in range(p):
            R.append(P[i] + Q[i])
        for i in range(p, q):
            R.append(P[i])
        
    quitaCeros(R)
    return R


# -Definimos la multiplicación de polinomos.
def multiPol(P, Q):
    p = len(P); q = len(Q)
    
    R = list()
    if p == 0 or q == 0:
        return R
    
    for i in range(p+q):
        R.append(0)
    
    for i in range(p):
        for j in range(q):
            R[i+j] += P[i]*Q[j]
            
    quitaCeros(R)
    return R


# -Función que divuelve el i-ésimo polinomio del ajuste de Lagrange.
def poliLagrange(i, x):
    n = len(x)
    Lx = list(); den = 0.0

    if n == 1:              # -Si sólo tenemos un termino, el ajuste es una  
        return Lx           #  constante.
    
    if i == 0:
        Lx.append(-x[1])
        Lx.append(1.0)
        den = x[0] - x[1]
        
        for j in range(1, n-1):
            Lx = multiPol(Lx, [-x[j+1], 1.0])
            den *= x[0] - x[j+1]
        
        Lx = multiPol(Lx, [1.0/den])    
        return Lx
    else:
        Lx.append(-x[0])
        Lx.append(1.0)
        den = x[i] - x[0]
        
        if i > 1:        
            for j in range(i-1):
                Lx = multiPol(Lx, [-x[j+1], 1.0])
                den *= x[i] - x[j+1]
        
        if i < n-1:
            for j in range(i, n - 1):
                Lx = multiPol(Lx, [-x[j+1], 1.0])
                den *= x[i] - x[j+1]
        
        Lx = multiPol(Lx, [1.0/den])    
        return Lx
    

# -Ajuste a polinomio. Devuelve un arreglo que representa el ajuste a 
#  polinomio resultado del método de Lagrange.
def ajustaPoli(x, y):
    n = len(x)
    polInter = list()
    lx = list()
    
    if n == 0:                  # -Si no hay datos que ajustar regresamos 
        return polInter         #  una lista vacia.
    
    if n == 1:                  # -Si tenemos sólo un dato regresamos 
        polInter.append(y[0])   #  la constante y[0]
        return polInter
    
    for i in range(n):
        lx = multiPol(poliLagrange(i, x), [y[i]])
        polInter = sumaPol(polInter, lx)
        
    return polInter
        

# -Evaluación del polinomio.
def poliEval(P,x):
    n = len(P)
    
    px = 0.0
    for i in range(n-1, -1, -1):
        px *= x
        px += P[i]
        
    return px


# -Derivada del polinomio.
def derivaPol(P):
    n = len(P)
    DP = list()
    
    if n == 0 or n == 1:
        return DP
    
    i = 1.0
    j = int(i)
    while j < n:
        DP.append(i*P[j])
        i += 1.0
        j = int(i)
        
    return DP


# -Newton-Rapson adaptado a estos polinomios.
def NewtonRapsonPol(P, x_0, a, b, epsilon):
    n = len(P)
    
    if n == 0 or n == 1:        # -Si el polinomio es una constante 
        return False            #  regresamos False.
    
    Dp = derivaPol(P)
    Nmax = 1000; x = x_0
    for i in range(Nmax):
        
        px = poliEval(P, x)
        if abs(px) <= epsilon:
            return x
        dp = poliEval(Dp, x)
        x += -px/dp
        
        if x < a:
            x = a
        if x > b:
            x = b
        
    return False                # -No se pudo encontrar raíz.


# -Esta función encuentra la derivada del polinomio dado para luego 
# -encontrar algún máximio (o mínimo) cercano a la semilla dada.
def encuentraMaxLocal(P, x_0, a, b):
    n = len(P)
    
    if n == 0 or n == 1:
        return False
    
    Dp = derivaPol(P)
    x = NewtonRapsonPol(Dp, x_0, a, b, 0.001)
    
    if not bool(x):
        print("No se pudo encontrar máximo local.")
        return False
    
    return x

        
# -Implementación a nuetro problema.
x = [0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0]
y = [10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]

p = ajustaPoli(x, y)            # -Polinomio interpolante.

# -Los arrelglos X,Y son para poder graficar.
Dx = 0.1; i = 0.0
X = list(); Y = list()
while(Dx*i < 200):
    xi = Dx*i
    X.append(xi)
    Y.append(poliEval(p, xi))
    i += 1.0


xlabel('x'); ylabel('f(x)'); title('Ajuste polinomio f(x) vs x')
plot(x, y, '.', lw = 2, color = 'r')
plot(X, Y, '-', lw = 2, color = 'b')
grid(True)
show()

# -Estimando energia de resonanacia.
E_r = encuentraMaxLocal(p, 75.0, 50.0, 100.0)
fmax = poliEval(p, E_r)
print("Punto de resonancia E_r = ", E_r) 
print("Valor en el punto de resonancia: f(E_r) = ", fmax)

q = list()
for i in range(len(p)):
    q.append(p[i])

# -Estimando Gamma.
q[0] -= fmax/2.0
xGamma1 = NewtonRapsonPol(q, 48.0, 40.0, 55.0, 0.001)
#print(xGamma1)
xGamma2 = NewtonRapsonPol(q, 107.0, 100.0, 115.0, 0.001)
#print(xGamma2)
print("Gamma = ", xGamma2 - xGamma1)