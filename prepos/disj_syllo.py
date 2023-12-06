'''
title: modus tollendo ponens (MTP)
other_names: Disjunctive syllogism
'''

from sympy import symbols

from barhana.rules import iff, theorem

p,q,r = symbols('p q')
pr = [
    p | q,
    ~p
]
conc = q
mtp = theorem(pr, conc)
