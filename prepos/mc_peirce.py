'''
title: Peirce's law
'''

from sympy import symbols

from barhana.rules import (claim_cons, ideriv, let_ante, let_not, modt,
                           theorem, vacuous)

p,q = symbols('p q')
pr = [
    (p >> q) >> p
]
conc = p
peirce = theorem(pr, conc)

if cl0 := conc: # p
    if1 = let_not(cl0) # ~p
    st1 = modt(pr[0], if1) # ~(p >> q)
    st2 = vacuous(if1, q) # p >> q
    pf0 = ideriv(if1, st1, st2) # p
