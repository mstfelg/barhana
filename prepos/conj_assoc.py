'''
title: Associative law for conjunction
'''

from sympy import symbols

from barhana.rules import iff, theorem

p,q,r = symbols('p q r')
pr = [
]
conc = iff(p & (q & r),  (p & q) & r)
conj_assoc = theorem(pr, conc)
