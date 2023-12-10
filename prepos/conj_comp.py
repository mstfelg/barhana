'''
title: Conjunction law of complement
other_names: Law of noncontradiction, Conjunction law of negation
desc: P and ~P is false.
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
conc = ~(p & ~p)
conj_neg = theorem(pr, conc)
