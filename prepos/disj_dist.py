'''
title: Distributitive law for disjunction
'''

from sympy import symbols

from barhana.rules import iff, theorem

p,q,r = symbols('p q r')
pr = [
]
conc = iff(p | (q & r), (p | q) & (p & r))
disj_dist = theorem(pr, conc)
