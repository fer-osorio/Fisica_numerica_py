#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:12:38 2021

@author: fernando
"""

from sympy import*

x, y, p, c = symbols('x, y, p, c')

y = 1/(x**2 + p**2 - 2*p*x*c)**(Rational(3, 2))
I1 = integrate(y, x)

pprint(I1)