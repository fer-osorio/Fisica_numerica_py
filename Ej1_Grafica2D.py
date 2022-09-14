# -*- coding: utf-8 -*-
"""
Created on Tuesday Aug 17 18:23 2021

@author: Fernando Osorio
"""

from pylab import *
Xmin = -5-0
Xmax = 5.0
Npoints = 500
Delta = (Xmax-Xmin)/Npoints
x = arange(Xmin, Xmax, Delta)
y = sin(x/4)*sin(2*x*x)

xlabel('x'); ylabel('f(x)'); title('f(x) vs x')
text(-1.50, 0.75, 'Ejemplo \n Mathplotlib')
plot(x, y, '-', lw = 1, color = 'b')
grid(True)
show()