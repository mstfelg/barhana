'''
title: Identity law for disjunction
'''

from sympy import false, symbols

from barhana.rules import iff, theorem

p = symbols('p')
pr = [
]
conc = iff(p | false, p)
conj_identity = theorem(pr, conc)
