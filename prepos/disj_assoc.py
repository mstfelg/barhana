'''
title: Associative law for disjunction
'''

from sympy import symbols

from barhana.rules import iff, theorem

p,q,r = symbols('p q r')
pr = [
]
conc = iff(p ^ (q ^ r),  (p ^ q) ^ r)
disj_assoc = theorem(pr, conc)
