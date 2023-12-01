'''
title: Law of totality
'''

from sympy import symbols

p,q,r = symbols('p q r')
pr = [
]
conc = (p >> q) | (q >> p)
