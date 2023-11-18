'''
title: Material Condition Import/Export
'''

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, modp, theorem, unconj

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r),
]
conc = (p & q) >> r
thm = theorem(pr, conc)

if cl0 := conc: # (p & q) >> r
    if1 = let_ante(cl0) # p & q

    if cl1 := claim_cons(cl0): # r
        st1,st2 = unconj(cl1) # p, q
        st3 = modp(st1, pr[0]) # q >> r
        pf1 = modp(st3, st2)
    pf0 = dderiv(if1, cl1)
