'''
title: Peirce's law
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, let_ante, theorem

p,q = symbols('p q')
pr = [
    (p >> q) >> p
]
conc = p
peirce = theorem(pr, conc)
