'''
title: Material implication
other_names: Conditional Equivalence, Or-and-if material condition
'''

from sympy import symbols

from barhana.rules import dneg, ideriv, iff, let_not, theorem, unconj, vacuous

p,q = symbols('p q')
pr = [
]
conc = iff(p >> q, ~p | q)
mc_impl = theorem(pr, conc)
