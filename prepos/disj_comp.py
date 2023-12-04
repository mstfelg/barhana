'''
title: Disjunction law of compliment
other_names: Law of excluded middle, Disjunction law of negation
desc: P or ~P
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
conc = p | ~p
conj_neg = theorem(pr, conc)
