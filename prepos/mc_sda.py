'''
title: Simplification of disjunctive antecedents
'''

from sympy import symbols

p,q,r = symbols('p q r')
pr = [
        (p ^ q) >> q
]
cl0 = (p >> r) ^ (q >> r)
