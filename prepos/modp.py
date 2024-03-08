'''
title: Modus Pollens
other_names: Law of detachment, Denying mode
'''

from sympy import symbols

from barhana.rules import dderiv, theorem

p,q = symbols('p q')
pr = [
    p,
    p >> q,
]
conc = q
modp = theorem(pr, conc)
