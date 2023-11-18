'''
title: Double negation
desc: Assume P iff ~~P.
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, iff, let_ante, theorem

p = symbols('p')
pr = [
    p
]
conc = iff(p, ~~p)
dneg = theorem(pr, conc)
