'''
title: Double negation
desc: Assume P iff ~~P.
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, iff, let_ante, theorem

p,q = symbols('p')
pr = [
    p
]
cl0 = iff(p, ~~p)
thm = theorem(pr, cl0)
