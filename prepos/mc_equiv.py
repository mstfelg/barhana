'''
title: Or-and-if material condition
other_names: Conditional Equivalence
'''

from sympy import symbols

from barhana.rules import *

p,q = symbols('p q')
pr = [
    p >> q
]
conc = ~p | q
mc_equiv = theorem(pr, conc)
