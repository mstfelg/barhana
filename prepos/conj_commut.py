'''
title: Commutative law for conjunction
'''

from sympy import symbols

from barhana.rules import iff, theorem

p,q = symbols('p q')
pr = [
]
conc = iff(p & q,  q & p)
conj_commut = theorem(pr, conc)
