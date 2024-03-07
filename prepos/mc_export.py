'''
title: Material Condition Export
other_names: Exportation
'''

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, modp, theorem, unconj

p,q,r = symbols('p q r')
pr = [
    (p & q) >> r
]
conc = p >> (q >> r)
mc_import = theorem(pr, conc)
