'''
title: Syllogism AAA-1
other_names: Syllogism Barbara
'''
from sympy import symbols

from barhana.rules import (claim_cons, dderiv, ideriv, let_ante, let_not, modp,
                           modt, theorem)

p,q,r = symbols('p q r')
pr = [
    p >> q
]
conc = (q >> r) >> (p >> r)
barbara = theorem(pr, conc)

if cl0 := conc:
    if1 = let_ante(cl0) # q >> r

    if cl1 := claim_cons(cl0): # p >> r
        if2 = let_ante(cl1) # p

        if cl2 := claim_cons(cl1): # r
            if3 = let_not(r)
            st1 = modt(cl1, if3) # ~p
            pf2 = ideriv(if2, st1) # r
        pf1 = dderiv(if2, cl2) # p >> r
    pf0 = dderiv(if1, cl1) # (q >> r) >> (p >> r)
