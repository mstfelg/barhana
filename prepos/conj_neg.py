'''
title: Conjunction law of negation
other_names: Law of noncontradiction
desc: P and ~P is false.
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
conc = ~(p & ~p)
conj_neg = theorem(pr, conc)
