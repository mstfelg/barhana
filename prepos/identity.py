'''
title: Law of identity
desc: P. Therefore P.
'''

from sympy import symbols

from barhana.rules import claim, dderiv, ideriv, let_not, theorem

p = symbols('p')
pr = [
    p
]
conc = p
thm = theorem(pr, conc)

# Direct proof

if cl0 := conc:
    pf1 = dderiv(cl0, pr[0])

# Indirect proof

if cl0 := conc:
    if1 = let_not(cl0)
    pf1 = ideriv(if1, pr[0])
