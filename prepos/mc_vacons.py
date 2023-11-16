'''
title: Vacuous consequent implication
desc: P. Therefore Q implies P.
'''

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, theorem

p,q = symbols('p q')
pr = [
    p
]
cl0 = q >> p
thm = theorem(pr, cl0)

if if1 := let_ante(cl0): # q
    cl1 = claim_cons(cl0) # p
pf1 = dderiv(cl1, pr[0])
