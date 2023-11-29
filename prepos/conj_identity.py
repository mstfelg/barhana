'''
title: Identity law for conjunction
'''

from sympy import symbols, true

from barhana.rules import iff, theorem

p = symbols('p')
pr = [
]
conc = iff(p & true, p)
conj_identity = theorem(pr, conc)
