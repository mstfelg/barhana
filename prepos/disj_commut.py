'''
title: Commutative law for disjunction
'''

from sympy import symbols

from barhana.rules import iff, theorem

p,q = symbols('p q')
pr = [
]
conc = iff(p ^ q,  q ^ p)
disj_commut = theorem(pr, conc)
