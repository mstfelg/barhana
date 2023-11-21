'''
title: Modus Tollens
other_names: Indirect reasoning
'''

from sympy import symbols

from barhana.rules import dderiv, theorem

p,q = symbols('p q')
pr = [
    ~q,
    p >> q,
]
conc = ~p
modt = theorem(pr, conc)
