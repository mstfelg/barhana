'''
title: Simplification of disjunctive antecedents
'''

from sympy import symbols

p,q,r = symbols('p q r')
pr = [
        (p | q) >> q
]
conc = (p >> r) | (q >> r)
