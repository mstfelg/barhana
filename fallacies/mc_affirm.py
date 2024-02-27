'''
title: Affirming the consequent
desc: P >> Q. Q. Not implies P.
'''

from barhana.rules import theorem
from sympy import symbols

p,q = symbols('p q')
pr = [
]
conc = ((p >> q) & q ) >> p
conc = ~conc
ac = theorem(pr, conc)
