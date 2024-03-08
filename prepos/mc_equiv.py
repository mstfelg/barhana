'''
title: Material equivalence
'''

from sympy import symbols

from barhana.rules import *

p,q = symbols('p q')
pr = [
]
conc = iff(iff(p, q), (p & q) | (~p & ~q))
mc_equiv = theorem(pr, conc)
