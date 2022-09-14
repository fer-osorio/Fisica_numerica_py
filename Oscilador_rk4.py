# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:31:02 2021

@author: 52954
"""

from pylab import *
# Definición de constantes
N=1000           # Número de pasos
x0=0.4           # Posición inicial
v0=0.0           # Velocidad inicial
tau=20.0          # Tiempo en segundos de la simulación
h=tau/float(N-1)   # Paso del tiempo
gravedad=9.8      # Aceleración 9.8 m/s**2
#mu = 0.15
k=15.0             # Constante elástica del resorte 
m=0.15             # Masa de la partícula
ni=0.055

# Generamos un arreglo de Nx2 para almacenar posición y velocidad
y=zeros([N,2])
# tomamos los valores del estado inicial
y[0,0]=x0
y[0,1]=v0

# Generamos tiempos igualmente espaciados
tiempo=linspace(0,tau,N)

def mu(v):
    return ni*abs(v)

# Definimos nuestra ecuación diferencial
def EDO(tiempo,estado):
    f0=estado[1]
    if f0 < 0:
        f1=-(k/m)*estado[0]+mu(f0)*gravedad
    else:
        f1=-(k/m)*estado[0]-mu(f0)*gravedad
    return array([f0,f1])

#Método de Rhonge-Kuta
def rk4Algor(t,h,N,y,f):
    k1=np.zeros(N); k2=np.zeros(N); k3=np.zeros(N); k4=np.zeros(N)
    k1 = h*f(t,y)                             
    k2 = h*f(t+h/2.,y+k1/2.)
    k3 = h*f(t+h/2.,y+k2/2.)
    k4 = h*f(t+h,y+k3)
    y=y+(k1+2*(k2+k3)+k4)/6.
    return y 


# Método de Euler para  resolver numéricamente la EDO 
#def Euler(y,t,h,f): 
#    y_s=y+h*f(y,t)  # Calculamos el valor siguiente de y
#    y_s=y+(f(y_s,t)+f(y,t))*h/2.0    
#    return y_s

# Ahora calculamos!
for j in range(N-1):
    y[j+1]=rk4Algor(tiempo[j],h,2,y[j],EDO)

# Ahora graficamos
xdatos=[y[j,0] for j in range(N)]
vdatos=[y[j,1] for j in range(N)]

plot(tiempo,xdatos,'-r')
plot(tiempo,vdatos,'-b')
#plot(xdatos,vdatos,'-b')
xlabel('Tiempo')
ylabel('Posición y velocidad')
show()