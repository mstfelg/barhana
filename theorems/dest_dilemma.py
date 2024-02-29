'''
title: Destructive dilemma
'''

from sympy import symbols

from barhana.rules import theorem

p,q,r,s = symbols('p q r s')
pr = [
    (p >> q) & (r >> s),
    ~q | ~s
]
conc = ~p | ~r
dest_dilemma = theorem(pr, conc)
