'''
title: Disjunction law of negation
other_names: Law of excluded middle
desc: P or ~P
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
conc = p | ~p
conj_neg = theorem(pr, conc)
