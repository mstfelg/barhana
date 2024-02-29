'''
title: Constructive dilemma
'''

from sympy import symbols

from barhana.rules import theorem

p,q,r,s = symbols('p q r s')
pr = [
    (p >> q) & (r >> s),
    p | r
]
conc = q | s
cons_dilemma = theorem(pr, conc)
